from rest_framework import serializers
from items.models import Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"
