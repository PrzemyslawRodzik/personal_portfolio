from django.http import HttpResponse
from django.shortcuts import render, redirect
from projects import models
from user_agents import parse

# Create your views here.
from projects.forms import ProjectForm
from projects.models import Project


def dodaj_bazy_view(request):
    project1 = models.Project(
        title='My 9 Project',
        description='9 web development project.',
        technology='Django',
        image='img/project1.jpg', )


    project1.save()
    
    return render(request, 'hello.html')


def project_index(request):
    projects = models.Project.objects.all().order_by('created_at').reverse()

    user_agent = parse(request.META['HTTP_USER_AGENT'])
    print(request.META['HTTP_USER_AGENT'])
    return render(request, 'projects/index.html', {'projects': projects, 'user_agent': user_agent})


def project_detail(request, id):
    selected_project = models.Project.objects.get(pk=id)
    print(selected_project.image)

    return render(request, 'projects/detail.html', {'selected_project': selected_project})


def create_view(request):
    blank_project_form = ProjectForm()
    if request.method == 'POST':
        upload = ProjectForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('project_index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'project_index'}}">reload</a>""")
    else:
        return render(request, 'projects/create_project.html', {'upload_form': blank_project_form})


def update_view(request, id):
    project_form = ProjectForm(request.POST or None, instance=Project.objects.get(id=id))
    if project_form.is_valid():
        project_form.save()
        return redirect('project_index')
    else:
        return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'project_index'}}">reload</a>""")


def edit_view(request, id):

    if request.method == 'GET':
        id = int(id)
        try:
            selected_project_to_change = Project.objects.get(id=id)
        except Project.DoesNotExist:
            return redirect('project_index')
        project_form = ProjectForm(request.POST or None, instance=selected_project_to_change)
        return render(request, 'projects/upload_form.html', {'upload_form': project_form, 'selected_project': selected_project_to_change})


def destroy_view(request, project_id):
    project_id = int(project_id)
    try:
        project_to_delete = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('project_index')
    project_to_delete.delete()
    return redirect('project_index')


def about_view(request):
    return render(request, 'projects/about.html')


