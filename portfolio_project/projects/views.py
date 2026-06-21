from django.shortcuts import render

# Create your views here.

from .models import Project

def projects_view(request):
    data = Project.objects.all()
    return render(request, 'projects/projects.html', {'data': data})
