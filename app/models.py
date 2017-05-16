from json import JSONEncoder
from time import time

class Jsonable:
    """Abstract class to standardize the toJson method to be implemented by any class that wants to be
    serialized to JSON"""

    def toJson(self):
        """Abstract method"""
        raise NotImplementedError('You should implement this method in your classes.')

class CommonMessage(Jsonable):
    def __init__(self):
        self.client = Client()
        self.emitter = Emitter()
        self.type = ""
        self.body = ""
        self.tags = ["music", "culture", "food"]

    def toJson(self):
        return dict(client=self.client, emitter=self.emitter, type=self.type, body=self.body, tags=self.tags)

class Client(Jsonable):
    def __init__(self):
        self.id = ""
        self.name = ""
        self.time = int(round(time() * 1000))

    def toJson(self):
        return dict(id=self.id, name=self.name, time=self.time)

class Emitter(Jsonable):
    def __init__(self):
        self.id = ""

    def toJson(self):
        return dict(id=self.id)

class ComplexJsonEncoder(JSONEncoder):
    """Basic JSON encoder for 'complex (nested)' Python objects."""

    def default(self, o):
        if hasattr(o, 'toJson'):
            return o.toJson()
        else:
            return JSONEncoder.default(self, o)
