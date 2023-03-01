from django.db import models


class SentimentAnalysis(models.Model):
    text = models.CharField(max_length=5000)
    prediction = models.CharField(max_length=5000)
