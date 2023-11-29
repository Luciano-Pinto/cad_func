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
    path('funcionarios/', views.funcionario_list, name='funcionarios'),
    path('funcionario_create/', views.funcionario_create, name='funcionario_create'),
    path('funcionario_update/<int:id>/', views.funcionario_update, name='funcionario_update'),
    path('funcionario_delete/<int:id>/', views.funcionario_delete, name='funcionario_delete'),

]
