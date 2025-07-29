from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'This is the first project',
    },
    {'id': '2',
     'title': 'Cloud Infrastructure',
     'description': 'This is the second project',
     },
    {
        'id': '3',
        'title': 'Machine Learning Model',
        'description': 'This is the third project',
    },

]


# def projects(request):
#     page = 'projects'
#     number = 10
#     context = {'page': page, 'number': number , 'projectList': projectList}
#     return render(request, 'projects/projects.html', context)
#
# def project(request,pk):
#     return render(request, 'projects/single-project.html' )

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)  # Fetch the project by its primary key (UUID)
    return render(request, 'projects/single-project.html', {'projectObj': projectObj })
