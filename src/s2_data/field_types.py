from abc import ABC, abstractmethod
from enum import IntFlag, IntEnum
import typing

class Type(ABC):
    @property
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def from_binary(self, binary: bytes) -> typing.Any:
        raise NotImplementedError()

    @abstractmethod
    def to_binary(self, value: typing.Any) -> bytes:
        raise NotImplementedError()

class BoolType(Type):
    @property
    def size(self):
        return 1

    def from_binary(self, binary):
        return binary[0] != 0

    def to_binary(self, value):
        return bytes([1 if value != 0 else 0])

class Int32Type(Type):
    @property
    def size(self):
        return 4

    def from_binary(self, binary):
        return int.from_bytes(binary, byteorder='little', signed=True)

    def to_binary(self, value):
        return value.to_bytes(length=self.size, byteorder='little', signed=True)

class UInt32Type(Type):
    @property
    def size(self):
        return 4

    def from_binary(self, binary):
        return int.from_bytes(binary, byteorder='little', signed=False)

    def to_binary(self, value):
        return value.to_bytes(length=self.size, byteorder='little', signed=False)

class Int64Type(Type):
    @property
    def size(self):
        return 8

    def from_binary(self, binary):
        return int.from_bytes(binary, byteorder='little', signed=True)

    def to_binary(self, value):
        return value.to_bytes(length=self.size, byteorder='little', signed=True)

class ByteType(Type):
    @property
    def size(self):
        return 1

    def from_binary(self, binary):
        return binary[0]

    def to_binary(self, value):
        return bytes([value])

class FlagType(Type):
    _size = None
    flag_definition = None

    def __init__(self, size, flag_definition):
        self._size = size
        self.flag_definition = flag_definition

    @property
    def size(self):
        return self._size

    def from_binary(self, binary):
        return self.flag_definition(int.from_bytes(binary, byteorder='little'))

    def to_binary(self, value):
        return value.to_bytes(length=self.size, byteorder='little')

class EnumType(Type):
    _size = None
    enum_definition = None

    def __init__(self, size, enum_definition):
        self._size = size
        self.enum_definition = enum_definition

    @property
    def size(self):
        return self._size

    def from_binary(self, binary):
        return self.enum_definition(int.from_bytes(binary, byteorder = 'little'))

    def to_binary(self, value):
        return value.to_bytes(length = self.size, byteorder = 'little')
