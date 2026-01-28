from typing import Optional
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from proxy import ProxyClient
from server import Command


class DataConsumer(JsonWebsocketConsumer):
    def connect(self) -> None:
        user: any = self.scope['user']
        if user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)('data', self.channel_name)
            self.accept()

    def disconnect(self, code: int) -> None:
        user: any = self.scope['user']
        if user.is_staff:
            async_to_sync(self.channel_layer.group_discard)('data', self.channel_name)

    def receive(self, text_data: Optional[str] = None, bytes_data: Optional[bytes] = None, **kwargs) -> None:
        proxy_client: ProxyClient = ProxyClient()
        if text_data == 'vol-down':
            proxy_client.send(Command.PLAYER_VOL_DOWN.value)
        elif text_data == 'vol-up':
            proxy_client.send(Command.PLAYER_VOL_UP.value)
        elif text_data == 'prev':
            proxy_client.send(Command.PLAYER_PREV.value)
        elif text_data == 'play':
            proxy_client.send(Command.PLAYER_PLAY.value)
        elif text_data == 'pause':
            proxy_client.send(Command.PLAYER_PAUSE.value)
        elif text_data == 'stop':
            proxy_client.send(Command.PLAYER_STOP.value)
        elif text_data == 'next':
            proxy_client.send(Command.PLAYER_NEXT.value)
        elif text_data == 'kill':
            proxy_client.send(Command.PLAYER_KILL.value)
        elif text_data == 'shutdown':
            proxy_client.send(Command.SHUTDOWN.value)

    def send_data(self, event: dict) -> None:
        self.send_json(event['content'])
