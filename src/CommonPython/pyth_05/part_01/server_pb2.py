# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x06report\"\x8b\x01\n\x0b\x43oordinates\x12\x13\n\x0b\x63oordinate1\x18\x01 \x01(\x05\x12\x13\n\x0b\x63oordinate2\x18\x02 \x01(\x05\x12\x13\n\x0b\x63oordinate3\x18\x03 \x01(\x02\x12\x13\n\x0b\x63oordinate4\x18\x04 \x01(\x05\x12\x13\n\x0b\x63oordinate5\x18\x05 \x01(\x05\x12\x13\n\x0b\x63oordinate6\x18\x06 \x01(\x02\"\xe2\x02\n\rSpaceshipInfo\x12\x32\n\talignment\x18\x01 \x01(\x0e\x32\x1f.report.SpaceshipInfo.Alignment\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06length\x18\x03 \x01(\x02\x12*\n\x05\x63lass\x18\x04 \x01(\x0e\x32\x1b.report.SpaceshipInfo.Class\x12\x0c\n\x04size\x18\x05 \x01(\x05\x12\r\n\x05\x61rmed\x18\x06 \x01(\x08\x12\x10\n\x08officers\x18\x07 \x03(\t\"*\n\tAlignment\x12\x08\n\x04none\x10\x00\x12\x08\n\x04\x61lly\x10\x01\x12\t\n\x05\x65nemy\x10\x02\"x\n\x05\x43lass\x12\r\n\tnoneclass\x10\x00\x12\x0c\n\x08\x43orvette\x10\x01\x12\x0b\n\x07\x46rigate\x10\x02\x12\x0b\n\x07\x43ruiser\x10\x03\x12\r\n\tDestroyer\x10\x04\x12\x0b\n\x07\x43\x61rrier\x10\x05\x12\x0f\n\x0b\x44readnought\x10\x06\x12\x0b\n\x07Unknown\x10\x07\x32\x46\n\x06Report\x12<\n\x0cGetSpaceship\x12\x13.report.Coordinates\x1a\x15.report.SpaceshipInfo\"\x00\x62\x06proto3')



_COORDINATES = DESCRIPTOR.message_types_by_name['Coordinates']
_SPACESHIPINFO = DESCRIPTOR.message_types_by_name['SpaceshipInfo']
_SPACESHIPINFO_ALIGNMENT = _SPACESHIPINFO.enum_types_by_name['Alignment']
_SPACESHIPINFO_CLASS = _SPACESHIPINFO.enum_types_by_name['Class']
Coordinates = _reflection.GeneratedProtocolMessageType('Coordinates', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATES,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:report.Coordinates)
  })
_sym_db.RegisterMessage(Coordinates)

SpaceshipInfo = _reflection.GeneratedProtocolMessageType('SpaceshipInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPACESHIPINFO,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:report.SpaceshipInfo)
  })
_sym_db.RegisterMessage(SpaceshipInfo)

_REPORT = DESCRIPTOR.services_by_name['Report']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COORDINATES._serialized_start=25
  _COORDINATES._serialized_end=164
  _SPACESHIPINFO._serialized_start=167
  _SPACESHIPINFO._serialized_end=521
  _SPACESHIPINFO_ALIGNMENT._serialized_start=357
  _SPACESHIPINFO_ALIGNMENT._serialized_end=399
  _SPACESHIPINFO_CLASS._serialized_start=401
  _SPACESHIPINFO_CLASS._serialized_end=521
  _REPORT._serialized_start=523
  _REPORT._serialized_end=593
# @@protoc_insertion_point(module_scope)
