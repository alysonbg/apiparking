from django.urls import path
from .views import CreateParking, ListParkingHistory

urlpatterns = [
    path('parking/', CreateParking.as_view()),
    path('parking/<str:plate>/', ListParkingHistory.as_view()),
]