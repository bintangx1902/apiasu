from rest_framework import serializers
from .models import *


class ICUSerializers(serializers.ModelSerializer):
    class Meta:
        model = ICUModels
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = IsolationRoom
        fields = '__all__'


class SpecialRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpecialRoom
        fields = '__all__'
