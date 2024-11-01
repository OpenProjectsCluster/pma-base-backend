import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title=os.getenv("PROJECT_NAME"),
    version=os.getenv("VERSION"),
    renderer_classes=[JSONOpenAPIRenderer],
)

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
