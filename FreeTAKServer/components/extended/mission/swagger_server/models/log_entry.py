# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LogEntry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, content: str=None, creator_uid: str=None, entry_uid: str=None, mission_names: List[str]=None, servertime: datetime=None, dtg: datetime=None, created: datetime=None, content_hashes: List[str]=None, keywords: List[str]=None):  # noqa: E501
        """LogEntry - a model defined in Swagger

        :param id: The id of this LogEntry.  # noqa: E501
        :type id: str
        :param content: The content of this LogEntry.  # noqa: E501
        :type content: str
        :param creator_uid: The creator_uid of this LogEntry.  # noqa: E501
        :type creator_uid: str
        :param entry_uid: The entry_uid of this LogEntry.  # noqa: E501
        :type entry_uid: str
        :param mission_names: The mission_names of this LogEntry.  # noqa: E501
        :type mission_names: List[str]
        :param servertime: The servertime of this LogEntry.  # noqa: E501
        :type servertime: datetime
        :param dtg: The dtg of this LogEntry.  # noqa: E501
        :type dtg: datetime
        :param created: The created of this LogEntry.  # noqa: E501
        :type created: datetime
        :param content_hashes: The content_hashes of this LogEntry.  # noqa: E501
        :type content_hashes: List[str]
        :param keywords: The keywords of this LogEntry.  # noqa: E501
        :type keywords: List[str]
        """
        self.swagger_types = {
            'id': str,
            'content': str,
            'creator_uid': str,
            'entry_uid': str,
            'mission_names': List[str],
            'servertime': datetime,
            'dtg': datetime,
            'created': datetime,
            'content_hashes': List[str],
            'keywords': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'content': 'content',
            'creator_uid': 'creatorUid',
            'entry_uid': 'entryUid',
            'mission_names': 'missionNames',
            'servertime': 'servertime',
            'dtg': 'dtg',
            'created': 'created',
            'content_hashes': 'contentHashes',
            'keywords': 'keywords'
        }
        self._id = id
        self._content = content
        self._creator_uid = creator_uid
        self._entry_uid = entry_uid
        self._mission_names = mission_names
        self._servertime = servertime
        self._dtg = dtg
        self._created = created
        self._content_hashes = content_hashes
        self._keywords = keywords

    @classmethod
    def from_dict(cls, dikt) -> 'LogEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LogEntry of this LogEntry.  # noqa: E501
        :rtype: LogEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this LogEntry.


        :return: The id of this LogEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this LogEntry.


        :param id: The id of this LogEntry.
        :type id: str
        """

        self._id = id

    @property
    def content(self) -> str:
        """Gets the content of this LogEntry.


        :return: The content of this LogEntry.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this LogEntry.


        :param content: The content of this LogEntry.
        :type content: str
        """

        self._content = content

    @property
    def creator_uid(self) -> str:
        """Gets the creator_uid of this LogEntry.


        :return: The creator_uid of this LogEntry.
        :rtype: str
        """
        return self._creator_uid

    @creator_uid.setter
    def creator_uid(self, creator_uid: str):
        """Sets the creator_uid of this LogEntry.


        :param creator_uid: The creator_uid of this LogEntry.
        :type creator_uid: str
        """

        self._creator_uid = creator_uid

    @property
    def entry_uid(self) -> str:
        """Gets the entry_uid of this LogEntry.


        :return: The entry_uid of this LogEntry.
        :rtype: str
        """
        return self._entry_uid

    @entry_uid.setter
    def entry_uid(self, entry_uid: str):
        """Sets the entry_uid of this LogEntry.


        :param entry_uid: The entry_uid of this LogEntry.
        :type entry_uid: str
        """

        self._entry_uid = entry_uid

    @property
    def mission_names(self) -> List[str]:
        """Gets the mission_names of this LogEntry.


        :return: The mission_names of this LogEntry.
        :rtype: List[str]
        """
        return self._mission_names

    @mission_names.setter
    def mission_names(self, mission_names: List[str]):
        """Sets the mission_names of this LogEntry.


        :param mission_names: The mission_names of this LogEntry.
        :type mission_names: List[str]
        """

        self._mission_names = mission_names

    @property
    def servertime(self) -> datetime:
        """Gets the servertime of this LogEntry.


        :return: The servertime of this LogEntry.
        :rtype: datetime
        """
        return self._servertime

    @servertime.setter
    def servertime(self, servertime: datetime):
        """Sets the servertime of this LogEntry.


        :param servertime: The servertime of this LogEntry.
        :type servertime: datetime
        """

        self._servertime = servertime

    @property
    def dtg(self) -> datetime:
        """Gets the dtg of this LogEntry.


        :return: The dtg of this LogEntry.
        :rtype: datetime
        """
        return self._dtg

    @dtg.setter
    def dtg(self, dtg: datetime):
        """Sets the dtg of this LogEntry.


        :param dtg: The dtg of this LogEntry.
        :type dtg: datetime
        """

        self._dtg = dtg

    @property
    def created(self) -> datetime:
        """Gets the created of this LogEntry.


        :return: The created of this LogEntry.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this LogEntry.


        :param created: The created of this LogEntry.
        :type created: datetime
        """

        self._created = created

    @property
    def content_hashes(self) -> List[str]:
        """Gets the content_hashes of this LogEntry.


        :return: The content_hashes of this LogEntry.
        :rtype: List[str]
        """
        return self._content_hashes

    @content_hashes.setter
    def content_hashes(self, content_hashes: List[str]):
        """Sets the content_hashes of this LogEntry.


        :param content_hashes: The content_hashes of this LogEntry.
        :type content_hashes: List[str]
        """

        self._content_hashes = content_hashes

    @property
    def keywords(self) -> List[str]:
        """Gets the keywords of this LogEntry.


        :return: The keywords of this LogEntry.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: List[str]):
        """Sets the keywords of this LogEntry.


        :param keywords: The keywords of this LogEntry.
        :type keywords: List[str]
        """

        self._keywords = keywords