from rest_framework import serializers
from .models import ImageClassification


class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = "__all__"
        read_only_fields = ["prediction"]
