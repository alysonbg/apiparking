from django.urls import path
from .views import CreateParking, ListParkingHistory, PayParking

urlpatterns = [
    path('parking/', CreateParking.as_view()),
    path('parking/<str:plate>/', ListParkingHistory.as_view()),
    path('parking/<int:pk>/pay/', PayParking.as_view()),
]