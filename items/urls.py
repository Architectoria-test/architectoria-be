from items.views import ItemViewSet, MaterialViewSet, OptionViewSet, BaseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'detail', ItemViewSet, basename='items')
router.register(r'material', MaterialViewSet, basename='materials')
router.register(r'option', OptionViewSet, basename='options')
router.register(r'base', BaseViewSet, basename='bases')

urlpatterns = router.urls
