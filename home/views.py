from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect


class Logout(View):

    def get(self, request):
        logout(request)
        print('aq')
        return redirect('home')
