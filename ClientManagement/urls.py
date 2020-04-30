from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include
import clients.urls as client_urls
import home.urls as home_urls
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('clients/', include(client_urls)),
    path('', include(home_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
