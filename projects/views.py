from django.shortcuts import render
from projects import models
from user_agents import parse

# Create your views here.


def dodaj_bazy_view(request):

    project1 = models.Project(
        title='My 8 Project',
        description='8 web development project.',
        technology='Laravel',
        image='img/project1.jpg',)


    project2 = models.Project(
        title='My 2 Project',
        description='Second development project.',
        technology='Vue',
        image='img/project2.jpg')
    project3 = models.Project(
                title='My Third Project',
                description='Third web development project.',
                technology='php',
                image='img/project3.jpg')
    project4 = models.Project(
        title='My 4 Project',
        description='4 web development project.',
        technology='Django',
        image='img/project4.jpg')
    project1.save()
    #project2.save()
    #project3.save()
    #project4.save()
    return render(request,'hello.html')


def project_index(request):
    projects = models.Project.objects.all().order_by('publication_date').reverse()

    user_agent = parse(request.META['HTTP_USER_AGENT'])
    print(request.META['HTTP_USER_AGENT'])
    print(request.META['REMOTE_ADDR'])
    print(request.META['REMOTE_HOST'])
    #print(request.META['REMOTE_USER'])

    return render(request, 'projects/index.html', {'projects': projects, 'user_agent': user_agent})


def project_detail(request, id):
    selected_project = models.Project.objects.get(pk=id)
    print(selected_project.image)

    return render(request, 'projects/detail.html', {'selected_project': selected_project})



