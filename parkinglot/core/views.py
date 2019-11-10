from rest_framework.views import APIView
from rest_framework import generics
from .models import Parking
from .serializers import ParkingSerializer, CreateParkingSerializer


class CreateParking(generics.CreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer
