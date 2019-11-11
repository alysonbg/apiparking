from rest_framework.views import APIView
from rest_framework import generics
from .models import Parking
from .serializers import ParkingSerializer, CreateParkingSerializer


class CreateParking(generics.CreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer


class ListParkingHistory(generics.ListAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        """Retorna todos estacionamentos para uma determinada placa"""
        plate = self.kwargs['plate']
        queryset = Parking.objects.filter(plate=plate)
        return queryset


class PayParking(generics.UpdateAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        """Paga o estacionamento"""
        id = self.kwargs['pk']
        parking = Parking.objects.get(id=id)
        queryset = Parking.objects.filter(id=id)
        if not parking.paid:
            parking.paid = True
            parking.save()

        return queryset


class LeaveParking(generics.UpdateAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        """Sai do estacionamento"""
        id = self.kwargs['pk']
        parking = Parking.objects.get(id=id)
        queryset = Parking.objects.filter(id=id)

        if parking.paid:
            parking.left = True
            parking.save()
        
        return queryset