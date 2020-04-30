import clients.urls as client_urls
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(client_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
