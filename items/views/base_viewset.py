from items.models import Base
from items.serializers import BaseSerializer
from .create_list_viewset import CreateListViewSet


class BaseViewSet(CreateListViewSet):
    serializer_class = BaseSerializer

    def get_queryset(self):
        return Base.objects.all()

