from django.db import models


class EnFrTranslation(models.Model):
    text = models.CharField(max_length=10000)
    prediction = models.CharField(max_length=10000)
