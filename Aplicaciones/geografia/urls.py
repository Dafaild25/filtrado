from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('listarPaises', views.listarPaises, name='listarPaises'),
    path('listarCiudades/<int:pais_id>/', views.listarCiudades, name='listarCiudades')
]