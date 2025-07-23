from django.urls import path

from projects import views
from projects.views import projects, project

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project' ),
]