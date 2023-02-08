from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('curso', views.curso,name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]

