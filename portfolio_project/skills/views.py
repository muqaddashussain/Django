from django.shortcuts import render

# Create your views here.

from .models import Skill

def skills_view(request):
    data = Skill.objects.all()
    return render(request, 'skills/skills.html', {'data': data})
