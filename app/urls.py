from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('modules.users.urls')),
    path('api/artist/', include('modules.artist.urls')),

    # Optional UI:
    path('api/swagger/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/swagger/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/swagger/schema/', SpectacularAPIView.as_view(), name='schema'),
]
