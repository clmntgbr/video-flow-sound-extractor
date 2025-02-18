# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMessage.proto\x12\x0c\x41pp.Protobuf\"?\n\x13\x41piToSoundExtractor\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"?\n\x13SoundExtractorToApi\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"B\n\x16\x41piToSubtitleGenerator\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"B\n\x16SubtitleGeneratorToApi\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"?\n\x13\x41piToSubtitleMerger\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"?\n\x13SubtitleMergerToApi\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"D\n\x18\x41piToSubtitleTransformer\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"D\n\x18SubtitleTransformerToApi\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"D\n\x18\x41piToSubtitleIncrustator\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"D\n\x18SubtitleIncrustatorToApi\x12(\n\x08mediaPod\x18\x01 \x01(\x0b\x32\x16.App.Protobuf.MediaPod\"\x8a\x01\n\x08MediaPod\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x10\n\x08userUuid\x18\x02 \x01(\t\x12*\n\roriginalVideo\x18\x03 \x01(\x0b\x32\x13.App.Protobuf.Video\x12\"\n\x05video\x18\x04 \x01(\x0b\x32\x13.App.Protobuf.Video\x12\x0e\n\x06status\x18\x05 \x01(\t\"\xad\x01\n\x05Video\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08mimeType\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0e\n\x06length\x18\x04 \x01(\x03\x12\x10\n\x08subtitle\x18\x05 \x01(\t\x12\x0b\n\x03\x61ss\x18\x06 \x01(\t\x12\x11\n\tsubtitles\x18\x07 \x03(\t\x12\x0e\n\x06\x61udios\x18\x08 \x03(\t\x12$\n\x06preset\x18\t \x01(\x0b\x32\x14.App.Protobuf.Preset\"\x8f\x02\n\x06Preset\x12\x14\n\x0csubtitleFont\x18\x01 \x01(\t\x12\x14\n\x0csubtitleSize\x18\x02 \x01(\t\x12\x15\n\rsubtitleColor\x18\x03 \x01(\t\x12\x1a\n\x12subtitleBackground\x18\x04 \x01(\t\x12\x1c\n\x14subtitleOutlineColor\x18\x05 \x01(\t\x12 \n\x18subtitleOutlineThickness\x18\x06 \x01(\t\x12\x16\n\x0esubtitleShadow\x18\x07 \x01(\t\x12\x1b\n\x13subtitleShadowColor\x18\x08 \x01(\t\x12\x17\n\x0fvideoResolution\x18\t \x01(\t\x12\x18\n\x10videoAspectRatio\x18\n \x01(\t*\xb6\x04\n\x0eMediaPodStatus\x12\x13\n\x0fUPLOAD_COMPLETE\x10\x00\x12\x1b\n\x17SOUND_EXTRACTOR_PENDING\x10\x01\x12\x1c\n\x18SOUND_EXTRACTOR_COMPLETE\x10\x02\x12\x19\n\x15SOUND_EXTRACTOR_ERROR\x10\x03\x12\x1e\n\x1aSUBTITLE_GENERATOR_PENDING\x10\x04\x12\x1f\n\x1bSUBTITLE_GENERATOR_COMPLETE\x10\x05\x12\x1c\n\x18SUBTITLE_GENERATOR_ERROR\x10\x06\x12\x1b\n\x17SUBTITLE_MERGER_PENDING\x10\x07\x12\x1c\n\x18SUBTITLE_MERGER_COMPLETE\x10\x08\x12\x19\n\x15SUBTITLE_MERGER_ERROR\x10\t\x12 \n\x1cSUBTITLE_TRANSFORMER_PENDING\x10\n\x12!\n\x1dSUBTITLE_TRANSFORMER_COMPLETE\x10\x0b\x12\x1e\n\x1aSUBTITLE_TRANSFORMER_ERROR\x10\x0c\x12 \n\x1cSUBTITLE_INCRUSTATOR_PENDING\x10\r\x12!\n\x1dSUBTITLE_INCRUSTATOR_COMPLETE\x10\x0e\x12\x1e\n\x1aSUBTITLE_INCRUSTATOR_ERROR\x10\x0f\x12\x0c\n\x08RESIZING\x10\x10\x12\x0b\n\x07RESIZED\x10\x11\x12\x14\n\x10READY_FOR_EXPORT\x10\x12\x12\t\n\x05\x45RROR\x10\x13\x42*\xca\x02\x0c\x41pp\\Protobuf\xe2\x02\x18\x41pp\\Protobuf\\GPBMetadatab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\312\002\014App\\Protobuf\342\002\030App\\Protobuf\\GPBMetadata'
  _MEDIAPODSTATUS._serialized_start=1299
  _MEDIAPODSTATUS._serialized_end=1865
  _APITOSOUNDEXTRACTOR._serialized_start=31
  _APITOSOUNDEXTRACTOR._serialized_end=94
  _SOUNDEXTRACTORTOAPI._serialized_start=96
  _SOUNDEXTRACTORTOAPI._serialized_end=159
  _APITOSUBTITLEGENERATOR._serialized_start=161
  _APITOSUBTITLEGENERATOR._serialized_end=227
  _SUBTITLEGENERATORTOAPI._serialized_start=229
  _SUBTITLEGENERATORTOAPI._serialized_end=295
  _APITOSUBTITLEMERGER._serialized_start=297
  _APITOSUBTITLEMERGER._serialized_end=360
  _SUBTITLEMERGERTOAPI._serialized_start=362
  _SUBTITLEMERGERTOAPI._serialized_end=425
  _APITOSUBTITLETRANSFORMER._serialized_start=427
  _APITOSUBTITLETRANSFORMER._serialized_end=495
  _SUBTITLETRANSFORMERTOAPI._serialized_start=497
  _SUBTITLETRANSFORMERTOAPI._serialized_end=565
  _APITOSUBTITLEINCRUSTATOR._serialized_start=567
  _APITOSUBTITLEINCRUSTATOR._serialized_end=635
  _SUBTITLEINCRUSTATORTOAPI._serialized_start=637
  _SUBTITLEINCRUSTATORTOAPI._serialized_end=705
  _MEDIAPOD._serialized_start=708
  _MEDIAPOD._serialized_end=846
  _VIDEO._serialized_start=849
  _VIDEO._serialized_end=1022
  _PRESET._serialized_start=1025
  _PRESET._serialized_end=1296
# @@protoc_insertion_point(module_scope)
