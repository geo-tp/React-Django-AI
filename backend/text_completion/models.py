from django.db import models


class EnTextCompletion(models.Model):
    text = models.CharField(max_length=5000)
    prediction = models.CharField(max_length=5000)
