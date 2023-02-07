from django.shortcuts import render
from django.http import HttpResponse

#from ProyectoCoder.AppCoder.models import Curso modifiqeste
from AppCoder.models import Curso

# Create your views here.
def curso(self):

    curso=Curso(nombre="desarrollo web",comision =19881)
    curso.save()
    documentoDeTexto=f'--> Curso:{curso.nombre} comision: {curso.comision}'
    return HttpResponse(documentoDeTexto)