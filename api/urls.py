from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', preview, name='preview'),
    path('icu', icu_list, name='icu'),
    path('icu/<int:pk>', icu_detail, name='icu-detail'),
    path('room', isolation_room_list, name='room'),
    path('s-room', special_room_list, name='s-room'),
]
