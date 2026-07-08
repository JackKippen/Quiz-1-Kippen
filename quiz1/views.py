from django.shortcuts import get_object_or_404, render

from .models import PersonalInformation, Project


def home(request):
    profile = PersonalInformation.objects.first()
    featured_projects = Project.objects.all()[:3]
    return render(request, 'home.html', {
        'personal_info': profile,
        'featured_projects': featured_projects,
    })


def about(request):
    profile = PersonalInformation.objects.first()
    return render(request, 'about.html', {'personal_info': profile})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def contact(request):
    profile = PersonalInformation.objects.first()
    return render(request, 'contact.html', {'personal_info': profile})


def personal_information(request):
    profile = PersonalInformation.objects.first()
    return render(request, 'personal_information.html', {'personal_info': profile})
