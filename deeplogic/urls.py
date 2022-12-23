
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pdfExtractor.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("files/", include('pdfExtractor.urls')),
    path("", homepage, name='homepage'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
