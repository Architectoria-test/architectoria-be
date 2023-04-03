from django.db import models
from .item_model import Item
from .create_update_model import CreateUpdateModel


class Property(CreateUpdateModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="property")
