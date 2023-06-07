from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.WorkForm import WorkForm
from datetime import datetime

from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from app.models.ProjectParticipant import ProjectParticipant
from app.models.ProjectSection import ProjectSection
from app.models.MaterialModel import MaterialModel
from ..forms.ProjectForm import ProjectForm, Project
from ..forms.ParticipantForm import ParticipantTypeForm
from app.forms.IndividualEntrepreneur import IndividualEntrepreneurForm
from app.forms.NaturalPerson import NaturalPersonForm
from app.forms.LegalEntity import LegalEntityForm


class ProjectView(View):
    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        projects = ProjectModel.objects.all().order_by('-id')

        return render(request, 'projects/Index.html', {'projects': projects})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)
        participants = ProjectParticipant.get_all_participants(project)
        sections = ProjectSection.objects.filter(project_id=project.id)
        sections_with_work = []
        for section in sections:
            work_count = WorkModel.objects.filter(projectSection__id=section.id).count()
            sections_with_work.append([section.id, section.name, work_count])
        materials = MaterialModel.objects.filter(work__projectSection__project_id=value)
        works = WorkModel.objects.filter(projectSection__project__id=value)
        work_form = WorkForm()
        data = {
            'project': project,
            'participants': participants,
            'individualEntrepreneur': IndividualEntrepreneurForm(),
            'naturalPerson': NaturalPersonForm(),
            'legalEntity': LegalEntityForm(),
            'participantType': ParticipantTypeForm(),
            'sections': sections_with_work,
            'workForm': work_form,
            'materials': materials,
            'works': works
        }

        return render(request, 'projects/View.html', data)

    @staticmethod
    def create_project(request: HttpRequest) -> HttpResponse:
        data = request.POST.get("project_name")
        project = ProjectModel(
            name_project=data
        )
        form = Project(instance=project)

        return render(request, 'projects/CreateProject.html', {'form': form})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = ProjectForm(request.POST)
        if form.is_valid():
            name_project = form.cleaned_data['name_project']
            name_project_documentation = form.cleaned_data['name_project_documentation']
            building_address = form.cleaned_data['building_address']
            date = datetime.now()
            project_code = form.cleaned_data['project_code']
            ProjectModel.objects.create(
                name_project=name_project,
                name_project_documentation=name_project_documentation,
                building_address=building_address,
                date=date,
                project_code=project_code
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

        # works = WorkModel.objects.filter(project=project)
        form = Project(instance=project)

        return render(request, 'projects/EditProject.html', {'project': project,
                                                      # 'works': works,
                                                      'form': form})


    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        project = ProjectModel.objects.get(id=value)
        project.delete()
        projects = ProjectModel.objects.all()

        return render(request, 'projects/Index.html', {'projects': projects})
