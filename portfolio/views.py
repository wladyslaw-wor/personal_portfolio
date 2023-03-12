from django.shortcuts import render
from .models import *

def home(request):
    projects = Project.objects.all()
    bio = Bio.objects.first()
    links = Link.objects.all()
    identics = Identic.objects.first()

    return render(request, 'portfolio/home.html', {'projects':projects, 'bio':bio, 'links':links, 'identic':identics})
