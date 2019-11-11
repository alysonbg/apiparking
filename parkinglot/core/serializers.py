import re
from rest_framework import serializers
from .models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'time', 'paid', 'left')


class CreateParkingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    plate = serializers.CharField(write_only=True)

    def validate_plate(self, plate):
        regex_validacao = re.compile('[A-Z]{3}-[0-9]{4}')

        if  not regex_validacao.match(plate):
            raise serializers.ValidationError(
               'A placa fornecida nao esta no formato AAA-9999'
            )
        return plate

    class Meta:
        model = Parking
        fields = ('id', 'plate')
        