from django.shortcuts import render

# Create your views here.

from .models import Education

def education_view(request):
    data = Education.objects.all()
    return render(request, 'education/education.html', {'data': data})
