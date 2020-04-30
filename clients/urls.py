from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import path

from .views import (
    CreateClient, DeleteClient, UpdateClient,
    ListClient, DetailClient
)

urlpatterns = [
    path('new/', login_required(CreateClient.as_view()), name='create_client'),
    path('', login_required(ListClient.as_view()), name='list_client'),
    path('delete/<int:pk>/', login_required(DeleteClient.as_view()), name='delete_client'),
    path('update/<int:pk>/', login_required(UpdateClient.as_view()), name='update_client'),
    path('detail/<int:pk>/', login_required(DetailClient.as_view()), name='detail_client'),
    path('doesnt_found/', login_required(TemplateView.as_view(template_name='clients/client_doesnt_found.html')), name='doesnt_found_client')  # noqa: E501
]
