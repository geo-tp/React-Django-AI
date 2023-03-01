from rest_framework import serializers
import json
from .models import ObjectDetection


class ObjectDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetection
        fields = "__all__"
        read_only_fields = ["prediction"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["prediction"] = json.loads(rep["prediction"])

        return rep
