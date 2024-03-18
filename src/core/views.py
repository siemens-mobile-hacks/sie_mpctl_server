from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ApplicationView(LoginRequiredMixin, View):
    login_url = '/admin/login/'

    @staticmethod
    def get(request: any) -> any:
        return render(request, 'application.html')
