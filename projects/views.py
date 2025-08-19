from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


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
    return render(request, 'projects/single-project.html', {'projectObj': projectObj})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect ('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

# if form.is_valid():
#     project = form.save(commit=False)
#     project.owner = request.user.profile  # or however you assign the user
#     project.save()
# Suppose your Project model has a field like owner, which is not part of the form (for example, set automatically to the logged-in user):

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project) # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)





