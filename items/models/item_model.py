from .base_instance_model import BaseInstance
from .slugify_model import Slugify
from .create_update_model import CreateUpdateModel


class Item(BaseInstance, Slugify, CreateUpdateModel):
    """
    Item model
    """
    pass
