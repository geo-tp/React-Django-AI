from rest_framework import serializers
from .models import EnTextCompletion


class EnTextCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnTextCompletion
        fields = "__all__"
        read_only_fields = ["prediction"]
