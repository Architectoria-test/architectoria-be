from rest_framework import serializers
from items.models import Item
from .property_serizlier import PropertySerializer


class ItemSerializer(serializers.ModelSerializer):
    property = PropertySerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = "__all__"
