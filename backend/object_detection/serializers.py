from rest_framework import serializers
import json
from .models import ObjectDetection


class ObjectDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetection
        fields = "__all__"
        read_only_fields = ["prediction"]

    def no_preds(self):
        return {
            "1": {
                "label": "Nothing Found",
                "percent": 100,
                "location": {"x1": 0, "y1": 0, "x2": 0, "y2": 0},
            }
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        json_preds = json.loads(rep["prediction"])

        rep["prediction"] = json_preds if json_preds else self.no_preds()

        return rep
