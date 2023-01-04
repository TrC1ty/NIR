from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.ProjectForm import ProjectForm
from ..forms.ParticipantForm import ParticipantForm
from app.models.ProjectModel import ProjectModel
from datetime import datetime


class ProjectView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        form = ProjectForm()

        return render(request, 'projects/creation.html', {'form': form})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = ProjectForm(request.POST)
        if form.is_valid():
            name_project = form.cleaned_data['name_project']
            name_project_documentation = form.cleaned_data['name_project_documentation']
            building_address = form.cleaned_data['building_address']
            date = datetime.now()
            number_document = form.cleaned_data['number_document']
            ProjectModel.objects.create(
                name_project=name_project,
                name_project_documentation=name_project_documentation,
                building_address=building_address,
                date=date,
                number_document=number_document
            ).save()

            return HttpResponseRedirect('projects/index')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        projects = ProjectModel.objects.all()

        return render(request, 'projects/index.html', {'projects': projects})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)

        return render(request, 'projects/project.html', {'project': project})
