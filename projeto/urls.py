from django.contrib import admin
from django.urls import path
from tenis.views import listar_tenis, detalhar_tenis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tenis/', listar_tenis),
    path('tenis/<int:id>', detalhar_tenis)
]
