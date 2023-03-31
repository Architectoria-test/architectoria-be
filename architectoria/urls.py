import os
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{os.environ.get("API_VERSION", "v1")}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'api/{os.environ.get("API_VERSION", "v1")}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
