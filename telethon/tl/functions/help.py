"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class GetAppChangelogRequest(TLObject):
    CONSTRUCTOR_ID = 0x9010ef6f
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, prev_app_version):
        """
        :param str prev_app_version:

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.prev_app_version = prev_app_version

    def to_dict(self):
        return {
            '_': 'GetAppChangelogRequest',
            'prev_app_version': self.prev_app_version
        }

    def __bytes__(self):
        return b''.join((
            b'o\xef\x10\x90',
            TLObject.serialize_bytes(self.prev_app_version),
        ))

    @staticmethod
    def from_reader(reader):
        _prev_app_version = reader.tgread_string()
        return GetAppChangelogRequest(prev_app_version=_prev_app_version)


class GetAppUpdateRequest(TLObject):
    CONSTRUCTOR_ID = 0xae2de196
    SUBCLASS_OF_ID = 0x5897069e

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetAppUpdateRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\x96\xe1-\xae',
        ))

    @staticmethod
    def from_reader(reader):
        return GetAppUpdateRequest()


class GetCdnConfigRequest(TLObject):
    CONSTRUCTOR_ID = 0x52029342
    SUBCLASS_OF_ID = 0xecda397c

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetCdnConfigRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'B\x93\x02R',
        ))

    @staticmethod
    def from_reader(reader):
        return GetCdnConfigRequest()


class GetConfigRequest(TLObject):
    CONSTRUCTOR_ID = 0xc4f9186b
    SUBCLASS_OF_ID = 0xd3262a4a

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetConfigRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'k\x18\xf9\xc4',
        ))

    @staticmethod
    def from_reader(reader):
        return GetConfigRequest()


class GetInviteTextRequest(TLObject):
    CONSTRUCTOR_ID = 0x4d392343
    SUBCLASS_OF_ID = 0xcf70aa35

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetInviteTextRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'C#9M',
        ))

    @staticmethod
    def from_reader(reader):
        return GetInviteTextRequest()


class GetNearestDcRequest(TLObject):
    CONSTRUCTOR_ID = 0x1fb33026
    SUBCLASS_OF_ID = 0x3877045f

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetNearestDcRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'&0\xb3\x1f',
        ))

    @staticmethod
    def from_reader(reader):
        return GetNearestDcRequest()


class GetRecentMeUrlsRequest(TLObject):
    CONSTRUCTOR_ID = 0x3dc0f114
    SUBCLASS_OF_ID = 0xf269c477

    def __init__(self, referer):
        """
        :param str referer:

        :returns help.RecentMeUrls: Instance of RecentMeUrls.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.referer = referer

    def to_dict(self):
        return {
            '_': 'GetRecentMeUrlsRequest',
            'referer': self.referer
        }

    def __bytes__(self):
        return b''.join((
            b'\x14\xf1\xc0=',
            TLObject.serialize_bytes(self.referer),
        ))

    @staticmethod
    def from_reader(reader):
        _referer = reader.tgread_string()
        return GetRecentMeUrlsRequest(referer=_referer)


class GetSupportRequest(TLObject):
    CONSTRUCTOR_ID = 0x9cdf08cd
    SUBCLASS_OF_ID = 0x7159bceb

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetSupportRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\xcd\x08\xdf\x9c',
        ))

    @staticmethod
    def from_reader(reader):
        return GetSupportRequest()


class GetTermsOfServiceRequest(TLObject):
    CONSTRUCTOR_ID = 0x350170f3
    SUBCLASS_OF_ID = 0x20ee8312

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetTermsOfServiceRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\xf3p\x015',
        ))

    @staticmethod
    def from_reader(reader):
        return GetTermsOfServiceRequest()


class SaveAppLogRequest(TLObject):
    CONSTRUCTOR_ID = 0x6f02f748
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, events):
        """
        :param list[InputAppEvent] events:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.events = events

    def to_dict(self):
        return {
            '_': 'SaveAppLogRequest',
            'events': [] if self.events is None else [None if x is None else x.to_dict() for x in self.events]
        }

    def __bytes__(self):
        return b''.join((
            b'H\xf7\x02o',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.events)),b''.join(bytes(x) for x in self.events),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _events = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _events.append(_x)

        return SaveAppLogRequest(events=_events)


class SetBotUpdatesStatusRequest(TLObject):
    CONSTRUCTOR_ID = 0xec22cfcd
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, pending_updates_count, message):
        """
        :param int pending_updates_count:
        :param str message:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.pending_updates_count = pending_updates_count
        self.message = message

    def to_dict(self):
        return {
            '_': 'SetBotUpdatesStatusRequest',
            'pending_updates_count': self.pending_updates_count,
            'message': self.message
        }

    def __bytes__(self):
        return b''.join((
            b'\xcd\xcf"\xec',
            struct.pack('<i', self.pending_updates_count),
            TLObject.serialize_bytes(self.message),
        ))

    @staticmethod
    def from_reader(reader):
        _pending_updates_count = reader.read_int()
        _message = reader.tgread_string()
        return SetBotUpdatesStatusRequest(pending_updates_count=_pending_updates_count, message=_message)