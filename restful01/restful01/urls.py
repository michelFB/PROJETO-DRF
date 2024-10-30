from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView,)


urlpatterns = [
     # Endpoint para gerar o token de autenticação
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path("admin/", admin.site.urls),
    path("", include("toys.urls")),
    path("api/", include("drones.urls")), 
    path("auth/", include("rest_framework.urls")),
    path("token/", views.obtain_auth_token),
    # Rota para o esquema OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    # Rota para o Swagger UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui',),
    ]
