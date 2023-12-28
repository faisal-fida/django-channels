from django.shortcuts import render
from .models import Room, Message


# Create your views here.
def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {"rooms": rooms})


def room(request, room_slug):
    room = Room.objects.get(slug=room_slug)
    messages = Message.objects.filter(room=room)
    return render(request, "chat/room.html", {"room": room, "messages": messages})
