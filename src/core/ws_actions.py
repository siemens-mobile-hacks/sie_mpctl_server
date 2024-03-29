from channels import layers
from asgiref.sync import async_to_sync


def ws_send_data(data: dict) -> None:
    channel_layer: any = layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)('data', {'type': 'send.data', 'content': data})
