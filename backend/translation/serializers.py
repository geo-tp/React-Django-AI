from rest_framework import serializers
from .models import EnFrTranslation


class EnFrTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnFrTranslation
        fields = "__all__"
        read_only_fields = ["prediction"]
