from django.urls import path, include
from django.contrib import admin

urlpatterns: list = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'))),
]
