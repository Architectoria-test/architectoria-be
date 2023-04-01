from django.db import models
from .create_update_model import CreateUpdateModel
from .property_model import Property


class Size(CreateUpdateModel):
    """
    Size model
    """
    length = models.PositiveIntegerField(verbose_name="Length")
    width = models.PositiveIntegerField(verbose_name="Width")
    percent_price = models.DecimalField(verbose_name="Percent price", max_digits=5, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="sizes")
