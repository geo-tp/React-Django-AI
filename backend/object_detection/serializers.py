from rest_framework import serializers
from .models import ObjectDetection


class ObjectDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetection
        fields = "__all__"
        read_only_fields = ["prediction"]
