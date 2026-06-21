from django.shortcuts import render

# Create your views here.

from .models import Bio

def bio_view(request):
    bio = Bio.objects.all()
    return render(request, 'bio/home.html', {'bio': bio})
