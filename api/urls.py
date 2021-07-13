from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', preview, name='preview'),
    path('icu', icu_list, name='icu'),
    path('room', isolation_room_list, name='room'),
    path('s-room', special_room_list, name='s-room'),
]
