from django.urls import path
from .views import UserApiView


urlpatterns = [

    path('login/', UserApiView.as_view()),
    path('login/<int:pk>', UserApiView.as_view()),
]
