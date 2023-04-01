from rest_framework import serializers
from items.models import Property
from .material_serializer import MaterialSerializer
from .size_serializer import SizeSerializer
from .option_serializer import OptionSerializer
from .base_serializer import BaseSerializer


class PropertySerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(read_only=False, many=True)
    sizes = SizeSerializer(read_only=False, many=True)
    options = OptionSerializer(read_only=False, many=True)
    bases = BaseSerializer(read_only=False, many=True)

    class Meta:
        model = Property
        fields = ("materials", "sizes", "options", "bases")
