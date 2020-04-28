from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DeleteView, DetailView, UpdateView, CreateView)
from .models import Client


class CreateClient(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('list_client')


class DeleteClient(DeleteView):
    model = Client
    success_url = reverse_lazy('list_client')


class UpdateClient(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('list_client')
    context_object_name = 'client'
    template_name = 'clients/client_update_form.html'


class DetailClient(DetailView):
    model = Client

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('doesnt_found_client')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ListClient(ListView):
    model = Client
    context_object_name = 'clients'
