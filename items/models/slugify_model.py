from django.db import models
from django.template.defaultfilters import slugify


class Slugify(models.Model):
    """
    Slugify model
    """
    slug = models.SlugField(verbose_name="Slug", max_length=256, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
