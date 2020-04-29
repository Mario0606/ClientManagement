from django.urls import path
from django.views.generic import TemplateView

from .views import (
    CreateClient, DeleteClient, UpdateClient,
    ListClient, DetailClient
)

urlpatterns = [
    path('new/', CreateClient.as_view(), name='create_client'),
    path('list/', ListClient.as_view(), name='list_client'),
    path('delete/<int:pk>/', DeleteClient.as_view(), name='delete_client'),
    path('update/<int:pk>/', UpdateClient.as_view(), name='update_client'),
    path('detail/<int:pk>/', DetailClient.as_view(), name='detail_client'),
    path('doesnt_found/', TemplateView.as_view(template_name='clients/client_doesnt_found.html'), name='doesnt_found_client')  # noqa: E501
]
