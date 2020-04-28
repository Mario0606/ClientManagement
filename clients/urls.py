from django.urls import path
from .views import (
    CreateClientView, DeleteClientView, UpdateClientView,
    ListClientView, DetailClientView
)

urlpatterns = [
    path('new/', CreateClientView.as_view(), name='create_client'),
    path('client/', DetailClientView.as_view(), name='detail_client'),
    path('delete/<int:id>/', CreateClientView.as_view(), name='delete_client'),
    path('update/<int:id>/', DeleteClientView.as_view(), name='update_client'),
    path('clients/<int:id>/', ListClientView.as_view(), name='list_client')
]
