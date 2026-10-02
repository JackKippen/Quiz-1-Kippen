from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('personal-information/', views.personal_information, name='personal_information'),
    path('contact/', views.inquiry_create, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/create/', views.testimony_create, name='testimony_create'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/projects/', views.project_dashboard_list, name='dashboard_projects'),
    path('dashboard/projects/create/', views.project_create, name='dashboard_project_create'),
    path('dashboard/tech-stacks/', views.tech_stack_dashboard_list, name='dashboard_tech_stacks'),
    path('dashboard/tech-stacks/create/', views.tech_stack_create, name='dashboard_tech_stack_create'),
    path('admin/', admin.site.urls),
]
