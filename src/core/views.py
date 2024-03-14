from django.views.generic import View
from django.shortcuts import render


class ApplicationView(View):
    @staticmethod
    def get(request: any) -> any:
        return render(request, 'application.html')
