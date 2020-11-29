from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from phone_verify.api import VerificationViewSet

from taxi.views import SignUpView, LogInView, ProfileView, image_upload
from .settings import VERSION

phone_router = routers.SimpleRouter()
phone_router.register(r'phone', VerificationViewSet, basename='phone')

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LogInView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    # path('auth/', include('rest_framework_social_oauth2.urls')),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('openapi', get_schema_view(
        title="Taxim taxis API",
        description="REST API",
        version=VERSION,
        public=True
    ), name='openapi-schema'),
    path('image/upload', image_upload, name='image-upload'),
    # path('health_check/', include('health_check.urls')),
]

urlpatterns += phone_router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)