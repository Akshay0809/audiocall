from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.pin_code = self.scope['url_route']['kwargs']['pin_code']
        self.room_group_name = f'call_{self.pin_code}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print('Disconnect')

    async def receive(self,text_data):
        receive_dict = json.loads(text_data)
        action=receive_dict['action']
        message = receive_dict.get('message', {})
        peer = receive_dict['peer']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
               'type': 'send_message',
                'action': action,
                'message': message,
                'peer': peer,
            }
        )

    async def send_sdp(self,event):
        receive_dict  = event['receive_dict']

        await self.send(text_data=json.dumps(receive_dict))
