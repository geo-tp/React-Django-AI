from rest_framework import serializers
from .models import SentimentAnalysis


class SentimentAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentAnalysis
        fields = "__all__"
        read_only_fields = ["prediction"]
