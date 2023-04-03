from rest_framework import serializers
from items.models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = "__all__"
