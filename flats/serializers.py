from rest_framework import serializers
from .models import ResaleFlat


class ResaleFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResaleFlat
        fields = "__all__"
