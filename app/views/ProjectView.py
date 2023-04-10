from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.ProjectForm import ProjectForm, Project
from ..forms.ParticipantForm import ParticipantForm, ParticipantTypeForm
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from datetime import datetime

from ..models.ProjectParticipant import ProjectParticipant
from ..forms.IndividualEntrepreneur import IndividualEntrepreneurForm
from ..forms.NaturalPerson import NaturalPersonForm
from ..forms.LegalEntity import LegalEntityForm


class ProjectView(View):
    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        projects = ProjectModel.objects.all().order_by('-id')

        return render(request, 'projects/index.html', {'projects': projects})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)
        participants = ProjectParticipant.get_all_participants(project)
        data = {
            'project': project,
            'participants': participants,
            'individualEntrepreneur': IndividualEntrepreneurForm(),
            'naturalPerson': NaturalPersonForm(),
            'legalEntity': LegalEntityForm(),
            'participantType': ParticipantTypeForm(),
        }

        return render(request, 'projects/project.html', data)

    @staticmethod
    def create_project(request: HttpRequest) -> HttpResponse:
        data = request.POST.get("project_name")
        project = ProjectModel(
            name_project=data
        )
        form = Project(instance=project)

        return render(request, 'projects/creation.html', {'form': form})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = ProjectForm(request.POST)
        print(123)
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

            return HttpResponseRedirect('/')

    @staticmethod
    def edit(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)

        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                project.name_project = form.cleaned_data['name_project']
                project.name_project_documentation = form.cleaned_data['name_project_documentation']
                project.building_address = form.cleaned_data['building_address']
                project.number_document = form.cleaned_data['number_document']
                project.save()

        works = WorkModel.objects.filter(project=project)
        form = Project(instance=project)

        return render(request, 'projects/edit.html', {'project': project,
                                                      'works': works,
                                                      'form': form})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)
        project.delete()
        projects = ProjectModel.objects.all()

        return render(request, 'projects/index.html', {'projects': projects})
