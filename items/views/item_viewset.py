from items.models import Item
from items.serializers import ItemSerializer
from .create_list_viewset import CreateListViewSet


class ItemViewSet(CreateListViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()
