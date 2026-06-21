from django.shortcuts import render

# Create your views here.

from .models import Experience

def experience_view(request):
    data = Experience.objects.all()
    return render(request, 'experience/experience.html', {'data': data})
