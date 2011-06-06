def my_view(request):
    return {'project':'Notify'}

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid_socketio.io import SocketIOContext, socketio_manage
import redis
from json import loads, dumps

@view_config(route_name = "home", renderer = "index.mk")
def home(request):
    return {'title':'Home', 'body':'Body'}

@view_config(route_name = "subscribe", renderer = "subscribe.mk")
def subscribe(request):
    if 'handle' in request.POST:
        uid = request.POST['handle']
        return HTTPFound(location = request.route_path('publisher', uid = uid))
    else:
        return {}

@view_config(route_name = "publisher", renderer = "publisher.mk")
def publisher(request):
    return {'uid': request.matchdict['uid']}

class ConnectIOContext(SocketIOContext):
    #self.io is the Socket.IO socket
    #self.request is the request
    
    def msg_connect(self, msg):
        print "Connect message received", msg
        msg = {'type': 'chat', 'uid': msg['uid']}
        self.r = redis.Redis()
        pubsub = self.r.pubsub()
        def listener():
            pubsub.subscribe([msg['uid']])
            for m in pubsub.listen():
                if not self.io.connected():
                    return
                print "From redis", m
                if m['type'] == 'message':
                    self.io.send(loads(m['data']))
        self.spawn(listener)
        #self.msg("chat", data = "data")

    def msg_chat(self, msg):
        print "New Chat message received", msg
        if msg.has_key('uid'):
            self.r.publish(msg['uid'], dumps(msg))

        #self.msg("chat", data = msg["data"], uid = msg["uid"])

@view_config(route_name = "socket.io")
def socketio_service(request):
    print "Socket.IO request running"
    retval = socketio_manage(ConnectIOContext(request))
    return Response(retval)
