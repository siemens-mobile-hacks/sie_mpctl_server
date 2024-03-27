from channels import layers

async def ws_send_data(data: dict) -> None:
    channel_layer: any = layers.get_channel_layer()
    await channel_layer.group_send('data', {'type': 'send.data', 'content': data})
