from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('modules.users.urls')),
    path('api/artist/', include('modules.artist.urls')),
    path('api/album/', include('modules.album.urls')),
    path('api/track/', include('modules.track.urls')),

    # Swagger:
    path('api/swagger/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/swagger/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/swagger/schema/', SpectacularAPIView.as_view(), name='schema'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]