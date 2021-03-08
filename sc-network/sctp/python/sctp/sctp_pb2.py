# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sctp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sctp.proto',
  package='sctp',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nsctp.proto\x12\x04sctp\"!\n\x10HandshakeRequest\x12\r\n\x05login\x18\x01 \x01(\t\"!\n\x11HandshakeResponse\x12\x0c\n\x04salt\x18\x01 \x01(\t\"$\n\x14\x41uthorizationRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"\x93\x01\n\x15\x41uthorizationResponse\x12\x36\n\x06status\x18\x02 \x01(\x0e\x32&.sctp.AuthorizationResponse.AuthStatus\x12\x10\n\x08\x63lientID\x18\x03 \x01(\r\"0\n\nAuthStatus\x12\n\n\x06\x46\x61iled\x10\x00\x12\x0b\n\x07Success\x10\x01\x12\t\n\x05\x45rror\x10\x02\"\xd2\x04\n\x15\x43reateElementsRequest\x12\x35\n\x08\x65lements\x18\x01 \x03(\x0b\x32#.sctp.CreateElementsRequest.Element\x1a\x14\n\x04Node\x12\x0c\n\x04type\x18\x01 \x01(\r\x1a\xb3\x01\n\x04\x45\x64ge\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x38\n\x06source\x18\x02 \x01(\x0b\x32(.sctp.CreateElementsRequest.Edge.Element\x12\x38\n\x06target\x18\x03 \x01(\x0b\x32(.sctp.CreateElementsRequest.Edge.Element\x1a)\n\x07\x45lement\x12\x0f\n\x07is_addr\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\r\x1a\x82\x01\n\x04Link\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x16\n\x0c\x62inary_value\x18\x05 \x01(\x0cH\x00\x42\x0f\n\rcontent_oneof\x1a\xb0\x01\n\x07\x45lement\x12\x30\n\x04node\x18\x01 \x01(\x0b\x32 .sctp.CreateElementsRequest.NodeH\x00\x12\x30\n\x04\x65\x64ge\x18\x02 \x01(\x0b\x32 .sctp.CreateElementsRequest.EdgeH\x00\x12\x30\n\x04link\x18\x03 \x01(\x0b\x32 .sctp.CreateElementsRequest.LinkH\x00\x42\x0f\n\relement_oneof\"\x18\n\x16\x43reateElementsResponse\"\xc1\x01\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12+\n\thandshake\x18\x15 \x01(\x0b\x32\x16.sctp.HandshakeRequestH\x00\x12*\n\x04\x61uth\x18\x16 \x01(\x0b\x32\x1a.sctp.AuthorizationRequestH\x00\x12-\n\x06\x63reate\x18\x17 \x01(\x0b\x32\x1b.sctp.CreateElementsRequestH\x00\x42\x0f\n\rrequest_oneof\"\xc6\x01\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12,\n\thandshake\x18\x15 \x01(\x0b\x32\x17.sctp.HandshakeResponseH\x00\x12+\n\x04\x61uth\x18\x16 \x01(\x0b\x32\x1b.sctp.AuthorizationResponseH\x00\x12.\n\x06\x63reate\x18\x17 \x01(\x0b\x32\x1c.sctp.CreateElementsResponseH\x00\x42\x10\n\x0eresponse_oneofb\x06proto3')
)



_AUTHORIZATIONRESPONSE_AUTHSTATUS = _descriptor.EnumDescriptor(
  name='AuthStatus',
  full_name='sctp.AuthorizationResponse.AuthStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failed', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Success', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Error', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=228,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_AUTHORIZATIONRESPONSE_AUTHSTATUS)


_HANDSHAKEREQUEST = _descriptor.Descriptor(
  name='HandshakeRequest',
  full_name='sctp.HandshakeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='sctp.HandshakeRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=53,
)


_HANDSHAKERESPONSE = _descriptor.Descriptor(
  name='HandshakeResponse',
  full_name='sctp.HandshakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='salt', full_name='sctp.HandshakeResponse.salt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=88,
)


_AUTHORIZATIONREQUEST = _descriptor.Descriptor(
  name='AuthorizationRequest',
  full_name='sctp.AuthorizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='sctp.AuthorizationRequest.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=126,
)


_AUTHORIZATIONRESPONSE = _descriptor.Descriptor(
  name='AuthorizationResponse',
  full_name='sctp.AuthorizationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='sctp.AuthorizationResponse.status', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientID', full_name='sctp.AuthorizationResponse.clientID', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTHORIZATIONRESPONSE_AUTHSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=276,
)


_CREATEELEMENTSREQUEST_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='sctp.CreateElementsRequest.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sctp.CreateElementsRequest.Node.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=379,
)

_CREATEELEMENTSREQUEST_EDGE_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='sctp.CreateElementsRequest.Edge.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_addr', full_name='sctp.CreateElementsRequest.Edge.Element.is_addr', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='sctp.CreateElementsRequest.Edge.Element.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=561,
)

_CREATEELEMENTSREQUEST_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='sctp.CreateElementsRequest.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sctp.CreateElementsRequest.Edge.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='sctp.CreateElementsRequest.Edge.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='sctp.CreateElementsRequest.Edge.target', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEELEMENTSREQUEST_EDGE_ELEMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=561,
)

_CREATEELEMENTSREQUEST_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='sctp.CreateElementsRequest.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sctp.CreateElementsRequest.Link.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='sctp.CreateElementsRequest.Link.int_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='sctp.CreateElementsRequest.Link.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='sctp.CreateElementsRequest.Link.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_value', full_name='sctp.CreateElementsRequest.Link.binary_value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content_oneof', full_name='sctp.CreateElementsRequest.Link.content_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=564,
  serialized_end=694,
)

_CREATEELEMENTSREQUEST_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='sctp.CreateElementsRequest.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='sctp.CreateElementsRequest.Element.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge', full_name='sctp.CreateElementsRequest.Element.edge', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='sctp.CreateElementsRequest.Element.link', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='element_oneof', full_name='sctp.CreateElementsRequest.Element.element_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=697,
  serialized_end=873,
)

_CREATEELEMENTSREQUEST = _descriptor.Descriptor(
  name='CreateElementsRequest',
  full_name='sctp.CreateElementsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='sctp.CreateElementsRequest.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEELEMENTSREQUEST_NODE, _CREATEELEMENTSREQUEST_EDGE, _CREATEELEMENTSREQUEST_LINK, _CREATEELEMENTSREQUEST_ELEMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=873,
)


_CREATEELEMENTSRESPONSE = _descriptor.Descriptor(
  name='CreateElementsResponse',
  full_name='sctp.CreateElementsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=875,
  serialized_end=899,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='sctp.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sctp.Request.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sctp.Request.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handshake', full_name='sctp.Request.handshake', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='sctp.Request.auth', index=3,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='sctp.Request.create', index=4,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request_oneof', full_name='sctp.Request.request_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=902,
  serialized_end=1095,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='sctp.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sctp.Response.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sctp.Response.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handshake', full_name='sctp.Response.handshake', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='sctp.Response.auth', index=3,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='sctp.Response.create', index=4,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response_oneof', full_name='sctp.Response.response_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1098,
  serialized_end=1296,
)

_AUTHORIZATIONRESPONSE.fields_by_name['status'].enum_type = _AUTHORIZATIONRESPONSE_AUTHSTATUS
_AUTHORIZATIONRESPONSE_AUTHSTATUS.containing_type = _AUTHORIZATIONRESPONSE
_CREATEELEMENTSREQUEST_NODE.containing_type = _CREATEELEMENTSREQUEST
_CREATEELEMENTSREQUEST_EDGE_ELEMENT.containing_type = _CREATEELEMENTSREQUEST_EDGE
_CREATEELEMENTSREQUEST_EDGE.fields_by_name['source'].message_type = _CREATEELEMENTSREQUEST_EDGE_ELEMENT
_CREATEELEMENTSREQUEST_EDGE.fields_by_name['target'].message_type = _CREATEELEMENTSREQUEST_EDGE_ELEMENT
_CREATEELEMENTSREQUEST_EDGE.containing_type = _CREATEELEMENTSREQUEST
_CREATEELEMENTSREQUEST_LINK.containing_type = _CREATEELEMENTSREQUEST
_CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_LINK.fields_by_name['int_value'])
_CREATEELEMENTSREQUEST_LINK.fields_by_name['int_value'].containing_oneof = _CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof']
_CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_LINK.fields_by_name['double_value'])
_CREATEELEMENTSREQUEST_LINK.fields_by_name['double_value'].containing_oneof = _CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof']
_CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_LINK.fields_by_name['string_value'])
_CREATEELEMENTSREQUEST_LINK.fields_by_name['string_value'].containing_oneof = _CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof']
_CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_LINK.fields_by_name['binary_value'])
_CREATEELEMENTSREQUEST_LINK.fields_by_name['binary_value'].containing_oneof = _CREATEELEMENTSREQUEST_LINK.oneofs_by_name['content_oneof']
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['node'].message_type = _CREATEELEMENTSREQUEST_NODE
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['edge'].message_type = _CREATEELEMENTSREQUEST_EDGE
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['link'].message_type = _CREATEELEMENTSREQUEST_LINK
_CREATEELEMENTSREQUEST_ELEMENT.containing_type = _CREATEELEMENTSREQUEST
_CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['node'])
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['node'].containing_oneof = _CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof']
_CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['edge'])
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['edge'].containing_oneof = _CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof']
_CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof'].fields.append(
  _CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['link'])
_CREATEELEMENTSREQUEST_ELEMENT.fields_by_name['link'].containing_oneof = _CREATEELEMENTSREQUEST_ELEMENT.oneofs_by_name['element_oneof']
_CREATEELEMENTSREQUEST.fields_by_name['elements'].message_type = _CREATEELEMENTSREQUEST_ELEMENT
_REQUEST.fields_by_name['handshake'].message_type = _HANDSHAKEREQUEST
_REQUEST.fields_by_name['auth'].message_type = _AUTHORIZATIONREQUEST
_REQUEST.fields_by_name['create'].message_type = _CREATEELEMENTSREQUEST
_REQUEST.oneofs_by_name['request_oneof'].fields.append(
  _REQUEST.fields_by_name['handshake'])
_REQUEST.fields_by_name['handshake'].containing_oneof = _REQUEST.oneofs_by_name['request_oneof']
_REQUEST.oneofs_by_name['request_oneof'].fields.append(
  _REQUEST.fields_by_name['auth'])
_REQUEST.fields_by_name['auth'].containing_oneof = _REQUEST.oneofs_by_name['request_oneof']
_REQUEST.oneofs_by_name['request_oneof'].fields.append(
  _REQUEST.fields_by_name['create'])
_REQUEST.fields_by_name['create'].containing_oneof = _REQUEST.oneofs_by_name['request_oneof']
_RESPONSE.fields_by_name['handshake'].message_type = _HANDSHAKERESPONSE
_RESPONSE.fields_by_name['auth'].message_type = _AUTHORIZATIONRESPONSE
_RESPONSE.fields_by_name['create'].message_type = _CREATEELEMENTSRESPONSE
_RESPONSE.oneofs_by_name['response_oneof'].fields.append(
  _RESPONSE.fields_by_name['handshake'])
_RESPONSE.fields_by_name['handshake'].containing_oneof = _RESPONSE.oneofs_by_name['response_oneof']
_RESPONSE.oneofs_by_name['response_oneof'].fields.append(
  _RESPONSE.fields_by_name['auth'])
_RESPONSE.fields_by_name['auth'].containing_oneof = _RESPONSE.oneofs_by_name['response_oneof']
_RESPONSE.oneofs_by_name['response_oneof'].fields.append(
  _RESPONSE.fields_by_name['create'])
_RESPONSE.fields_by_name['create'].containing_oneof = _RESPONSE.oneofs_by_name['response_oneof']
DESCRIPTOR.message_types_by_name['HandshakeRequest'] = _HANDSHAKEREQUEST
DESCRIPTOR.message_types_by_name['HandshakeResponse'] = _HANDSHAKERESPONSE
DESCRIPTOR.message_types_by_name['AuthorizationRequest'] = _AUTHORIZATIONREQUEST
DESCRIPTOR.message_types_by_name['AuthorizationResponse'] = _AUTHORIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateElementsRequest'] = _CREATEELEMENTSREQUEST
DESCRIPTOR.message_types_by_name['CreateElementsResponse'] = _CREATEELEMENTSRESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandshakeRequest = _reflection.GeneratedProtocolMessageType('HandshakeRequest', (_message.Message,), dict(
  DESCRIPTOR = _HANDSHAKEREQUEST,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.HandshakeRequest)
  ))
_sym_db.RegisterMessage(HandshakeRequest)

HandshakeResponse = _reflection.GeneratedProtocolMessageType('HandshakeResponse', (_message.Message,), dict(
  DESCRIPTOR = _HANDSHAKERESPONSE,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.HandshakeResponse)
  ))
_sym_db.RegisterMessage(HandshakeResponse)

AuthorizationRequest = _reflection.GeneratedProtocolMessageType('AuthorizationRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUTHORIZATIONREQUEST,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.AuthorizationRequest)
  ))
_sym_db.RegisterMessage(AuthorizationRequest)

AuthorizationResponse = _reflection.GeneratedProtocolMessageType('AuthorizationResponse', (_message.Message,), dict(
  DESCRIPTOR = _AUTHORIZATIONRESPONSE,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.AuthorizationResponse)
  ))
_sym_db.RegisterMessage(AuthorizationResponse)

CreateElementsRequest = _reflection.GeneratedProtocolMessageType('CreateElementsRequest', (_message.Message,), dict(

  Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELEMENTSREQUEST_NODE,
    __module__ = 'sctp_pb2'
    # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest.Node)
    ))
  ,

  Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(

    Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), dict(
      DESCRIPTOR = _CREATEELEMENTSREQUEST_EDGE_ELEMENT,
      __module__ = 'sctp_pb2'
      # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest.Edge.Element)
      ))
    ,
    DESCRIPTOR = _CREATEELEMENTSREQUEST_EDGE,
    __module__ = 'sctp_pb2'
    # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest.Edge)
    ))
  ,

  Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELEMENTSREQUEST_LINK,
    __module__ = 'sctp_pb2'
    # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest.Link)
    ))
  ,

  Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), dict(
    DESCRIPTOR = _CREATEELEMENTSREQUEST_ELEMENT,
    __module__ = 'sctp_pb2'
    # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest.Element)
    ))
  ,
  DESCRIPTOR = _CREATEELEMENTSREQUEST,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.CreateElementsRequest)
  ))
_sym_db.RegisterMessage(CreateElementsRequest)
_sym_db.RegisterMessage(CreateElementsRequest.Node)
_sym_db.RegisterMessage(CreateElementsRequest.Edge)
_sym_db.RegisterMessage(CreateElementsRequest.Edge.Element)
_sym_db.RegisterMessage(CreateElementsRequest.Link)
_sym_db.RegisterMessage(CreateElementsRequest.Element)

CreateElementsResponse = _reflection.GeneratedProtocolMessageType('CreateElementsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEELEMENTSRESPONSE,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.CreateElementsResponse)
  ))
_sym_db.RegisterMessage(CreateElementsResponse)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'sctp_pb2'
  # @@protoc_insertion_point(class_scope:sctp.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
