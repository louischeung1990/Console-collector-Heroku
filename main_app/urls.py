from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('consoles/', views.consoles_index, name='index'),
    path('consoles/<int:console_id>/', views.console_detail, name="detail"),
]