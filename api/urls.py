from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'api'

urlpatterns = [
    path('', preview, name='preview'),
    path('icu', icu_list, name='icu'),
    path('icu/<int:pk>', icu_detail, name='icu-detail'),
    path('room', isolation_room_list, name='room'),
    path('room/<int:pk>', isolation_room_detail, name='room-detail'),
    path('s-room', special_room_list, name='s-room'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
