from django.urls import path
from core.views import ApplicationView

urlpatterns: list = [
    path('', ApplicationView.as_view()),
]
