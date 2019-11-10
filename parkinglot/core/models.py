from django.db import models


class Parking(models.Model):
    plate = models.CharField(max_length=8)
    time = models.TimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
