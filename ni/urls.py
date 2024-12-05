# ni/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'admin Django
    path('api/', include('myproject.urls')),  # Inclure les URLs de l'application systems
]
