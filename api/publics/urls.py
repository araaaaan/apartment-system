from django.urls import path

from .views import PublicUserDetailView

urlpatterns = [
    # path('', RoomAPIView.as_view()),
    path('/<int:pk>', PublicUserDetailView.as_view())
]