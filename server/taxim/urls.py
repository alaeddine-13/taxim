from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from taxi.views import SignUpView, LogInView
from .settings import VERSION


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LogInView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    path('swagger-ui/', TemplateView.as_view(
        template_name='templates/swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='templates/redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('openapi', get_schema_view(
        title="Taxim taxis API",
        description="REST API",
        version=VERSION
    ), name='openapi-schema'),
]
