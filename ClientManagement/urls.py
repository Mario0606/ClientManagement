import clients.urls as client_urls
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(client_urls))
]
