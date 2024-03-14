from django.urls import path
from django.contrib import admin

urlpatterns: list = [
    path('admin/', admin.site.urls),
]
