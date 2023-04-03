from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

API_VERSION = settings.API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_VERSION}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_VERSION}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{API_VERSION}/items/', include('items.urls'))
]
