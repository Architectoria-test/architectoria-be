from django.db import models


class BaseInstance(models.Model):
    """
    Base model
    """
    title = models.CharField(verbose_name="Title", max_length=256)
    image = models.URLField(verbose_name="Image url", max_length=512)
    price = models.DecimalField(verbose_name="Price", max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
