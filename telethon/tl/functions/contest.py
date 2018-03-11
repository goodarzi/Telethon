"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class SaveDeveloperInfoRequest(TLObject):
    CONSTRUCTOR_ID = 0x9a5f6e95
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, vk_id, name, phone_number, age, city):
        """
        :param int vk_id:
        :param str name:
        :param str phone_number:
        :param int age:
        :param str city:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.vk_id = vk_id
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.city = city

    def to_dict(self):
        return {
            '_': 'SaveDeveloperInfoRequest',
            'vk_id': self.vk_id,
            'name': self.name,
            'phone_number': self.phone_number,
            'age': self.age,
            'city': self.city
        }

    def __bytes__(self):
        return b''.join((
            b'\x95n_\x9a',
            struct.pack('<i', self.vk_id),
            TLObject.serialize_bytes(self.name),
            TLObject.serialize_bytes(self.phone_number),
            struct.pack('<i', self.age),
            TLObject.serialize_bytes(self.city),
        ))

    @staticmethod
    def from_reader(reader):
        _vk_id = reader.read_int()
        _name = reader.tgread_string()
        _phone_number = reader.tgread_string()
        _age = reader.read_int()
        _city = reader.tgread_string()
        return SaveDeveloperInfoRequest(vk_id=_vk_id, name=_name, phone_number=_phone_number, age=_age, city=_city)