from django.shortcuts import render
from .models import Skill, Project, Achievement


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
        'achievements': achievements,
        'current_year': 2025
    })

# Create your views here.
