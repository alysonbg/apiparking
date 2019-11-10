from rest_framework import serializers
from .models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'time', 'paid', 'left')


class CreateParkingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    plate = serializers.CharField(write_only=True)
    class Meta:
        model = Parking
        fields = ('id', 'plate')

        