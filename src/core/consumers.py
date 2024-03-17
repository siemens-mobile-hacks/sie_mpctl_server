from typing import Optional
from channels.generic.websocket import JsonWebsocketConsumer
from proxy import ProxyClient
from server import Command


class DataConsumer(JsonWebsocketConsumer):
    def connect(self) -> None:
        user: any = self.scope['user']
        if True:
            self.accept()
            # while True:
            #     await self.send_json({})
            #     await asyncio.sleep(1)

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
