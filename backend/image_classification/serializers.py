from rest_framework import serializers
from .models import ImageClassification
import json


class ImageClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClassification
        fields = "__all__"
        read_only_fields = ["prediction"]

    def no_preds(self):
        return {
            "1": {
                "label": "Nothing Found",
                "percent": 100,
            }
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        json_preds = json.loads(rep["prediction"])
        rep["prediction"] = json_preds if json_preds else self.no_preds()

        return rep
