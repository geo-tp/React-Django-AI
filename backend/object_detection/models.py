from django.db import models


class ObjectDetection(models.Model):
    img = models.ImageField()
    prediction = models.CharField(max_length=250)
