from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def preview(request):
    api = {
        'ICU API': '/api/icu',
        'Isolation Room API': '/api/room/',
        'Special Room API': '/api/s-room/',
    }
    return Response(api)


@api_view(['GET', 'POST'])
def icu_list(request):
    if request.method == 'GET':
        icu = ICUModels.objects.all()
        serializer = ICUSerializers(icu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ICUSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def icu_detail(request, pk):

    try:
        icu = get_object_or_404(ICUModels, pk=pk)
    except ICUModels.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ICUSerializers(icu, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ICUSerializers(icu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        icu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def isolation_room_list(request):
    room = IsolationRoom.objects.all()
    serializer = RoomSerializers(room, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def isolation_room_detail(request, pk):
    room = get_object_or_404(IsolationRoom, pk=pk)
    serializer = RoomSerializers(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def special_room_list(request):
    s_room = SpecialRoom.objects.all()
    serializer = SpecialRoomSerializers(s_room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def special_room_detail(request, pk):
    s_room = get_object_or_404(SpecialRoom, pk=pk)
    serializer = SpecialRoomSerializers(s_room, many=False)
    return Response(serializer.data)
