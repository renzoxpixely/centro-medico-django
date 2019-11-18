from django.shortcuts import render

from .models import Project

# Create your views here.
def reserva(request):
    projects = Project.objects.all()
  