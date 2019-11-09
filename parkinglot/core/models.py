from django.db import models


class Parking(models.Model):
    plate = models.CharField(max_length=8)
    time = models.TimeField()
    paid = models.BooleanField()
    left = models.BooleanField()
