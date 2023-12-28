from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:room_slug>/", views.room, name="room"),
]
