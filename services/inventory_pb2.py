# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"\x17\n\x06Number\x12\r\n\x05input\x18\x01 \x01(\x05\"\x18\n\x06Result\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x19\n\x08\x42ookIsbn\x12\r\n\x05input\x18\x01 \x01(\t\"\xa6\x01\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x10\n\x08pub_year\x18\x04 \x01(\x05\x12\x1e\n\x05genre\x18\x05 \x01(\x0e\x32\x0f.Book.GenreEnum\"A\n\tGenreEnum\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0b\n\x07\x46ICTION\x10\x01\x12\x0e\n\nNONFICTION\x10\x02\x12\n\n\x06HORROR\x10\x03\"\x1f\n\rResultAddBook\x12\x0e\n\x06result\x18\x01 \x01(\t\"\xb0\x01\n\rInventoryItem\x12\x18\n\x10inventory_number\x18\x01 \x01(\t\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x15\n\x04\x62ook\x18\x03 \x01(\x0b\x32\x05.BookH\x00\x12%\n\x06status\x18\x04 \x01(\x0e\x32\x15.InventoryItem.Status\"/\n\x06Status\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\t\n\x05TAKEN\x10\x02\x42\x06\n\x04type2+\n\rAddOneService\x12\x1a\n\x06\x61\x64\x64One\x12\x07.Number\x1a\x07.Number2L\n\x0b\x42ookService\x12 \n\x07\x61\x64\x64\x42ook\x12\x05.Book\x1a\x0e.ResultAddBook\x12\x1b\n\x07getBook\x12\t.BookIsbn\x1a\x05.Bookb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NUMBER._serialized_start=19
  _NUMBER._serialized_end=42
  _RESULT._serialized_start=44
  _RESULT._serialized_end=68
  _BOOKISBN._serialized_start=70
  _BOOKISBN._serialized_end=95
  _BOOK._serialized_start=98
  _BOOK._serialized_end=264
  _BOOK_GENREENUM._serialized_start=199
  _BOOK_GENREENUM._serialized_end=264
  _RESULTADDBOOK._serialized_start=266
  _RESULTADDBOOK._serialized_end=297
  _INVENTORYITEM._serialized_start=300
  _INVENTORYITEM._serialized_end=476
  _INVENTORYITEM_STATUS._serialized_start=421
  _INVENTORYITEM_STATUS._serialized_end=468
  _ADDONESERVICE._serialized_start=478
  _ADDONESERVICE._serialized_end=521
  _BOOKSERVICE._serialized_start=523
  _BOOKSERVICE._serialized_end=599
# @@protoc_insertion_point(module_scope)