from digitalpy.core.parsing.load_configuration import Configuration
from .model_constants import EventVariables as vars
import uuid
from datetime import datetime as dt
import datetime
from FreeTAKServer.components.core.abstract_component.cot_node import CoTNode
from FreeTAKServer.components.core.abstract_component.cot_property import CoTProperty


class Event(CoTNode):
    # TODO: fix emergency methods
    # Event.py
    """Python implementation of the Class Event
    # represents a TAK event: this class is instantiated with a standard set of
    #    values.
    # Generated by Enterprise Architect
    # Created on: 11-Feb-2020 11:08:07 AM
    # Original author: Corvo
    """

    # event as an XML
    # <?xml version="1.0" encoding="UTF-8" standalone="yes"?><event version="2.0" uid="Linux-ABC.server-ping" type="b-t-f" time="2020-02-14T20:32:31.444Z" start="2020-02-14T20:32:31.444Z" stale="2020-02-15T20:32:31.444Z" how="h-g-i-g-o">

    # default constructor

    def __init__(self, configuration: Configuration, model, oid=None):

        super().__init__(self.__class__.__name__, configuration, model, oid)
        self.cot_attributes["version"] = None
        self.cot_attributes["uid"] = None
        self.cot_attributes["type"] = None
        self.cot_attributes["how"] = None
        self.cot_attributes["stale"] = None
        self.cot_attributes["start"] = None
        self.cot_attributes["time"] = None

        # flag to determin e if this event is a geo chcat if so, will be added as a
        # prefix to the uid

        # starting time when an event should be considered valid
        start = "%Y-%m-%dT%H:%M:%SZ"
        # basic event
        # Gives a hint about how the coordinates were generated

        # Schema version of this event instance (e.g.  2.0)

        # time stamp: when the event was generated
        time = "%Y-%m-%dT%H:%M:%SZ"

        # Hierarchically organized hint about event type (defaultis is 'a-f-G-I'
        # for infrastructure)

        # ending time when an event should no longer be considered valid
        stale = "%Y-%m-%dT%H:%M:%SZ"

        # Globally unique name for this information on this event can have
        # additional information attached.
        # e.g.  -ping means that this request is a ping

        # flag to determine if this event is a Ping, in this case append to the UID

    @CoTProperty
    def start(self):
        return self.cot_attributes.get("start", None)

    @start.setter
    def start(self, start=0):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if start == None:
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.cot_attributes["start"] = zulu
        else:
            self.cot_attributes["start"] = start

    @CoTProperty
    def how(self):
        return self.cot_attributes.get("how", None)

    @how.setter
    def how(self, how=0):
        self.cot_attributes["how"] = how

    @CoTProperty
    def uid(self):
        return self.cot_attributes.get("uid", None)

    @uid.setter
    def uid(self, uid):
        if uid == None:
            self.uid = str(uuid.uuid1())

        else:
            self.cot_attributes["uid"] = uid

    @CoTProperty
    def version(self):
        return self.cot_attributes.get("version", None)

    @version.setter
    def version(self, version):
        self.cot_attributes["version"] = version

    @CoTProperty
    def time(self):
        return self.cot_attributes.get("time", None)

    @time.setter
    def time(self, time=0):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if time == None:
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.time = zulu
        else:
            self.cot_attributes["time"] = time

    @CoTProperty
    def stale(self):
        return self.cot_attributes.get("stale", None)

    @stale.setter
    def stale(self, stale=None):
        # for case where stale is explicitly stated as a string
        if isinstance(stale, str):
            self.cot_attributes["stale"]=stale
        # for case where a int representing the timeout is passed
        elif isinstance(stale,int):
            DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            add = datetime.timedelta(seconds=stale)
            stale_part = dt.strptime(zulu, DATETIME_FMT) + add
            self.cot_attributes["stale"] = stale_part.strftime(DATETIME_FMT)

    @CoTProperty
    def type(self):
        return self.cot_attributes.get("type", None)

    @type.setter
    def type(self, type=0):
        self.cot_attributes["type"] = type

    @CoTProperty
    def point(self):
        return self.cot_attributes.get("point", None)

    @point.setter
    def point(self, point=None):
        self.cot_attributes["point"] = point

    @CoTProperty
    def detail(self):
        return self.cot_attributes.get("detail", None)

    @detail.setter
    def detail(self, detail=None):
        self.cot_attributes["detail"] = detail
