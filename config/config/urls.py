from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path

api_app_patterns: list[URLPattern | URLResolver] = [
    path("users/", include("apps.users.api.root.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_app_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
