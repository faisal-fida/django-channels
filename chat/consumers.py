# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room = data["room"]

        await self.save_message(
            self,
            message,
            username,
            room,
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "message",
                "message": message,
                "username": username,
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @async_to_sync
    def save_message(self, message, username, room):
        room = Room.objects.get(slug=room)
        Message.objects.create(user=username, room=room, content=message)
