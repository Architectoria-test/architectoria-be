from items.models import Material
from items.serializers import MaterialSerializer
from .create_list_viewset import CreateListViewSet


class MaterialViewSet(CreateListViewSet):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        return Material.objects.all()

