from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView

from .models import PersonalInformation, Project, Testimony, Inquiry
from .forms import ProjectForm, InquiryForm, TestimonyForm


def home(request):
    profile = PersonalInformation.objects.first()
    featured_projects = Project.objects.all()[:3]
    # lightweight stats and preview data for the homepage
    latest_testimonies = Testimony.objects.order_by('-created_at')[:3]
    projects_count = Project.objects.count()
    skills = ['HTML', 'Django', 'C++', 'Python', 'Git']
    years_learning = 1

    # prepare simple tech lists for featured projects
    featured_projects_with_techs = []
    for p in featured_projects:
        techs = [t.strip() for t in p.tech_stack.split(',')] if p.tech_stack else []
        featured_projects_with_techs.append({'project': p, 'techs': techs})

    return render(request, 'home.html', {
        'personal_info': profile,
        'featured_projects': featured_projects_with_techs,
        'latest_testimonies': latest_testimonies,
        'projects_count': projects_count,
        'skills': skills,
        'skills_count': len(skills),
        'years_learning': years_learning,
    })


def about(request):
    profile = PersonalInformation.objects.first()
    return render(request, 'about.html', {'personal_info': profile})


def projects(request):
    projects = Project.objects.all()
    projects_with_techs = []
    for p in projects:
        techs = [t.strip() for t in p.tech_stack.split(',')] if p.tech_stack else []
        projects_with_techs.append({'project': p, 'techs': techs})
    return render(request, 'projects.html', {'projects': projects_with_techs})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def inquiry_create(request):
    profile = PersonalInformation.objects.first()
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_create.html', {'form': form, 'personal_info': profile})


def personal_information(request):
    profile = PersonalInformation.objects.first()
    return render(request, 'personal_information.html', {'personal_info': profile})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonies_list.html'
    context_object_name = 'testimonies'
    ordering = ['-created_at']


def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimony_detail.html', {'testimony': testimony})


def testimony_create(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            testimony = form.save()
            return redirect('testimony_detail', pk=testimony.pk)
    else:
        form = TestimonyForm()
    return render(request, 'testimony_create.html', {'form': form})
