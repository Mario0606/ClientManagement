from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DeleteView, DetailView, UpdateView, CreateView)
from .models import Client


class CreateClientView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('create_client')


class DeleteClientView(DeleteView):
    model = Client
    success_url = reverse_lazy('delete_client')


class UpdateClientView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('update_client')


class DetailClientView(DetailView):
    model = Client


class ListClientView(ListView):
    model = Client
