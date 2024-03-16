import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class DataConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self) -> None:
        user: any = self.scope['user']
        if user.is_staff:
            await self.accept()
            while True:
                await self.send_json({})
                await asyncio.sleep(1)
