import json
from app.models import *

class MessageController:

    def on_get(self, req, resp):
        """Handle GET requests for messages"""
        msg = CommonMessage()
        print(msg)
        testMsg = {'msg': 'msg'}
        testMsgJson = json.dumps(msg.toJson(), cls=ComplexJsonEncoder)
        print(f"Json message: {testMsgJson}")
        resp.body = testMsgJson
