from rest_framework import serializers
from .models import ImageClassification
import json


class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = "__all__"
        read_only_fields = ["prediction"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["prediction"] = json.loads(rep["prediction"])

        return rep
