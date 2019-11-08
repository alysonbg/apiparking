from django.db import models


class Parking(models.Model):
    plate = models.CharField(max=8, required=True)
    time = models.TimeField()
    paid = models.BooleanField()
    left = models.BooleanField()
