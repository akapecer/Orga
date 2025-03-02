from django.urls import path
from . import views

urlpatterns = [
    path('genera-pdf-menu/<int:menu_id>/', views.genera_pdf_menu, name='genera_pdf_menu'),
]
