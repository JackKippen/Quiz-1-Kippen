from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from .forms import (
    AdminOnlyAuthenticationForm,
    InquiryForm,
    ProjectForm,
    TechStackForm,
    TestimonyForm,
    UserRegisterForm,
)
from .models import Inquiry, PersonalInformation, Project, TechStack, Testimony


def home(request):
    profile = PersonalInformation.objects.first()
    featured_projects = Project.objects.prefetch_related('tech_stacks').all()[:3]
    latest_testimonies = Testimony.objects.order_by('-created_at')[:3]
    projects_count = Project.objects.count()
    skills = ['HTML', 'Django', 'C++', 'Python', 'Git']
    years_learning = 1

    featured_projects_with_techs = []
    for project in featured_projects:
        featured_projects_with_techs.append({
            'project': project,
            'techs': [tech.name for tech in project.tech_stacks.all()],
        })

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
    projects = Project.objects.prefetch_related('tech_stacks').all()
    projects_with_techs = []
    for project in projects:
        projects_with_techs.append({
            'project': project,
            'techs': [tech.name for tech in project.tech_stacks.all()],
        })
    return render(request, 'projects.html', {'projects': projects_with_techs})


class AdminLoginView(LoginView):
    template_name = 'login.html'
    form_class = AdminOnlyAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account created successfully. Please sign in as the admin.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def logout_page(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('home')

    return render(request, 'logout.html')


@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def dashboard(request):
    projects = Project.objects.prefetch_related('tech_stacks').all()
    tech_stacks = TechStack.objects.prefetch_related('projects').all()
    project_rows = []
    for project in projects:
        project_rows.append({
            'project': project,
            'techs': [tech.name for tech in project.tech_stacks.all()],
        })

    tech_rows = []
    for tech_stack in tech_stacks:
        tech_rows.append({
            'tech_stack': tech_stack,
            'project_names': [project.project_name for project in tech_stack.projects.all()],
        })

    return render(request, 'dashboard.html', {'projects': project_rows, 'tech_stacks': tech_rows})


@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def project_dashboard_list(request):
    projects = Project.objects.prefetch_related('tech_stacks').all()
    project_rows = []
    for project in projects:
        project_rows.append({
            'project': project,
            'techs': [tech.name for tech in project.tech_stacks.all()],
        })
    return render(request, 'dashboard_projects.html', {'projects': project_rows})


@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def tech_stack_dashboard_list(request):
    tech_stacks = TechStack.objects.prefetch_related('projects').all()
    tech_rows = []
    for tech_stack in tech_stacks:
        tech_rows.append({
            'tech_stack': tech_stack,
            'project_names': [project.project_name for project in tech_stack.projects.all()],
        })
    return render(request, 'dashboard_tech_stacks.html', {'tech_stacks': tech_rows})


@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            selected_stack = form.cleaned_data['tech_stacks']
            project.tech_stacks.add(selected_stack)
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})


@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def tech_stack_create(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            tech_stack = form.save()
            return redirect('dashboard_tech_stacks')
    else:
        form = TechStackForm()
    return render(request, 'techstack_create.html', {'form': form})


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
