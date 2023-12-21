from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("chat/", include("chat.urls")),
]
