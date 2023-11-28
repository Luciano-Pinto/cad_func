from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cad_func'

urlpatterns = [
    path('', views.home, name='home'),
    path('setores/', views.setor_list, name='setores'),
    path('setor_create/', views.setor_create, name='setor_create'),
    path('setor_update/<int:id>/', views.setor_update, name='setor_update'),
    path('setor_delete/<int:id>/', views.setor_delete, name='setor_delete'),
]
