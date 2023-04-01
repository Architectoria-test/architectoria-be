from items.models import Option
from items.serializers import OptionSerializer
from .create_list_viewset import CreateListViewSet


class OptionViewSet(CreateListViewSet):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.all()

