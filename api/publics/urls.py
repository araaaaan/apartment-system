from django.urls import path

from .views import RoomAPIView

urlpatterns = [
    path('', RoomAPIView.as_view()),
]