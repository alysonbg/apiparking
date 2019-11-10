from django.urls import path
from .views import CreateParking

urlpatterns = [
    path('parking/', CreateParking.as_view()),
]