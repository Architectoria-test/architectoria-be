from django.db import models
from .base_instance_model import BaseInstance
from .create_update_model import CreateUpdateModel
from .slugify_model import Slugify
from .property_model import Property


class Material(BaseInstance, Slugify, CreateUpdateModel):
    """
    Material model
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="materials")
