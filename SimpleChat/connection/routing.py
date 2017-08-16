from channels.routing import route
from connection.consumers import ws_connect, ws_message

channel_routing = [
	route("websocket.connect", ws_connect, path=r"^/connection/[a-zA-Z0-9_]+$"),
    route("websocket.receive", ws_message),
]