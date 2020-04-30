from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import Logout
from django.urls import path

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('logout/', Logout.as_view(), name='logout')
]