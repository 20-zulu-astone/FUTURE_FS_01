from django.shortcuts import render
from .models import Skill, Project, Achievement

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
        'achievements': achievements
    })

# Create your views here.
