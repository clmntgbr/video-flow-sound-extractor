import os
import re
import ffmpeg

from kombu import Queue
from flask import Flask
from celery import Celery
from pydub import AudioSegment

from src.config import Config
from src.s3_client import S3Client
from src.rabbitmq_client import RabbitMQClient
from src.file_client import FileClient
from src.converter import ProtobufConverter
from src.Protobuf.Message_pb2 import ApiToSoundExtractor, MediaPodStatus, MediaPod

app = Flask(__name__)
app.config.from_object(Config)
s3_client = S3Client(Config)
rmq_client = RabbitMQClient()
file_client = FileClient()

celery = Celery("tasks", broker=app.config["RABBITMQ_URL"])

celery.conf.update(
    {
        "task_serializer": "json",
        "accept_content": ["json"],
        "broker_connection_retry_on_startup": True,
        "task_routes": {
            "tasks.process_message": {"queue": app.config["RMQ_QUEUE_WRITE"]}
        },
        "task_queues": [
            Queue(
                app.config["RMQ_QUEUE_READ"], routing_key=app.config["RMQ_QUEUE_READ"]
            )
        ],
    }
)


@celery.task(name="tasks.process_message", queue=app.config["RMQ_QUEUE_READ"])
def process_message(message):
    mediaPod: MediaPod = ProtobufConverter.json_to_protobuf(message)
    protobuf = ApiToSoundExtractor()
    protobuf.mediaPod.CopyFrom(mediaPod)
    protobuf.IsInitialized()

    try:
        id = os.path.splitext(protobuf.mediaPod.originalVideo.name)[0]
        type = os.path.splitext(protobuf.mediaPod.originalVideo.name)[1]

        key = f"{protobuf.mediaPod.userUuid}/{protobuf.mediaPod.uuid}/{protobuf.mediaPod.originalVideo.name}"
        keyFrame = f"{protobuf.mediaPod.userUuid}/{protobuf.mediaPod.uuid}/{id}.jpg"
        tmpFilePath = f"/tmp/{protobuf.mediaPod.originalVideo.name}"
        tmpFramePath = f"/tmp/{id}.jpg"

        if not s3_client.download_file(key, tmpFilePath):
            return False

        audioFilePath = id + ".mp3"
        tmpAudioFilePath = f"/tmp/{audioFilePath}"

        probe = ffmpeg.probe(tmpFilePath)
        duration = float(probe["format"]["duration"])

        if not extract_sound(tmpFilePath, tmpAudioFilePath):
            return False

        if not extract_frame(tmpFilePath, tmpFramePath, duration):
            return False

        audioFilePath = convert_to_wav(tmpAudioFilePath)

        chunks = chunk_wav(audioFilePath, id)

        for chunk in chunks:
            key = (
                f"{protobuf.mediaPod.userUuid}/{protobuf.mediaPod.uuid}/audios/{chunk}"
            )
            if not s3_client.upload_file(f"/tmp/{chunk}", key):
                return False
            file_client.delete_file(f"/tmp/{chunk}")

        if not s3_client.upload_file(tmpFramePath, keyFrame):
            return False
        
        file_client.delete_file(tmpAudioFilePath)
        file_client.delete_file(tmpFilePath)
        file_client.delete_file(tmpFramePath)

        resultsSorted = sorted(chunks, key=extract_chunk_number)

        protobuf.mediaPod.frame = f"{id}.jpg"
        protobuf.mediaPod.originalVideo.length = int(duration)
        protobuf.mediaPod.originalVideo.audios.extend(resultsSorted)
        protobuf.mediaPod.status = MediaPodStatus.Name(
            MediaPodStatus.SOUND_EXTRACTOR_COMPLETE
        )

        rmq_client.send_message(protobuf, "App\\Protobuf\\SoundExtractorToApi")

        return True
    except Exception:
        protobuf.mediaPod.status = MediaPodStatus.Name(
            MediaPodStatus.SOUND_EXTRACTOR_ERROR
        )
        if not rmq_client.send_message(protobuf, "App\\Protobuf\\SoundExtractorToApi"):
            return False


def extract_sound(file: str, audioFilePath: str) -> bool:
    try:
        ffmpeg.input(file).output(f"{audioFilePath}").run()
        print(f"audio successfully extracted: {audioFilePath}")
        return True
    except Exception as e:
        print(f"error extracting audio: {e}")
    return False


def extract_frame(file: str, tmpFramePath: str, duration: float) -> bool:
    try:
        middle_time = duration / 2
        time_str = f"{int(middle_time // 3600):02}:{int((middle_time % 3600) // 60):02}:{int(middle_time % 60):02}"
        ffmpeg.input(file, ss=time_str).output(tmpFramePath, vframes=1, pix_fmt='yuv420p', format='image2', update='1').run()
        return True
    except Exception as e:
        print(f"error extracting audio: {e}")
    return False


def extract_chunk_number(item):
    match = re.search(r"_(\d+)\.wav$", item[0])
    return int(match.group(1)) if match else float("inf")


def convert_to_wav(audioFilePath: str) -> str:
    wav_path = audioFilePath.replace(".mp3", ".wav")
    ffmpeg.input(audioFilePath).output(wav_path, ac=1, ar=16000, y=None).run(quiet=True)
    return wav_path


def chunk_wav(audioFilePath: str, uuid: str) -> list[str]:
    audio = AudioSegment.from_mp3(audioFilePath)
    segmentDuration = 5 * 60 * 1000
    chunkFilenames = []

    chunks = [
        audio[i : i + segmentDuration] for i in range(0, len(audio), segmentDuration)
    ]
    for idx, chunk in enumerate(chunks):
        chunk.export(f"/tmp/{uuid}_{idx+1}.wav", format="wav")
        chunkFilenames.append(f"{uuid}_{idx+1}.wav")

    return chunkFilenames
