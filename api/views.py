from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def preview(request):
    api = {
        'ICU API': '/api/icu',
        'Isolation Room API': '/api/room/',
        'Special Room API': '/api/s-room/',
    }
    return Response(api)


@api_view(['GET'])
def icu_list(request):
    icu = ICUModels.objects.all()
    serializer = ICUSerializers(icu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def isolation_room_list(request):
    room = IsolationRoom.objects.all()
    serializer = RoomSerializers(room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def special_room_list(request):
    s_room = SpecialRoom.objects.all()
    serializer = SpecialRoomSerializers(s_room, many=True)
    return Response(serializer.data)
