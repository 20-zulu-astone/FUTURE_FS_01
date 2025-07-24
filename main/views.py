from django.shortcuts import render
from .models import Skill, Project, Achievement
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Optionally process/store/send this data
        print(f"New message from {name} ({email}): {message}")
        messages.success(request, "Thanks for reaching out. I'll get back to you soon!")

    return render(request, 'contact.html')

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    skills = Skill.objects.all().order_by('name')
    return render(request, 'skills.html')

def project(request):
    project = Project.objects.all()
    return render(request, 'projects.html',{'project':project})

def achievements(request):
    achievement = Achievement.objects.all().order_by('-date')
    return render(request, 'achievements.html',{'achievement':achievement})


   

   

