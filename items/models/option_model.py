from django.db import models
from .create_update_model import CreateUpdateModel
from .property_model import Property
from .base_instance_model import BaseInstance


class Option(BaseInstance, CreateUpdateModel):
    """
    Option model
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="options")
