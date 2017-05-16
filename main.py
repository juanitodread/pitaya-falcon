import falcon
from app.controllers import MessageController

app = falcon.API()

app.add_route('/api/messages', MessageController())