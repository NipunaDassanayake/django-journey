from django.http import HttpResponse
from django.shortcuts import render

projectList = [
    {
        'id' : '1',
        'title' : 'Ecommerce Website',
        'description' : 'This is the first project',
    },
    {        'id' : '2',
        'title' : 'Cloud Infrastructure',
        'description' : 'This is the second project',
    },
    {
        'id' : '3',
        'title' : 'Machine Learning Model',
        'description' : 'This is the third project',
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
    page = 'Projects'
    number = 10
    context = {'page': page, 'number': number , 'projectList': projectList}

    return render(request, 'projects/projects.html',context)

def project(request , pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i


    return render(request,'projects/single-project.html', {'projectObj': projectObj})