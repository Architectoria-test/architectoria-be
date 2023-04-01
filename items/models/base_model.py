from django.db import models
from .base_instance_model import BaseInstance
from .create_update_model import CreateUpdateModel
from .property_model import Property


class Base(BaseInstance, CreateUpdateModel):
    """
    Base model
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bases")
