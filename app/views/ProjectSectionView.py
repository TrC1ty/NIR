from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from app.models.ProjectModel import ProjectModel
from ..models.ProjectSection import ProjectSection


class ProjectSectionView(View):
    @staticmethod
    def post(request: HttpRequest, project_id) -> HttpResponse:
        form = request.POST.dict()
        project = ProjectModel.objects.get(id=project_id)
        ProjectSection.objects.create(
            project=project,
            name=form['section_name']
        )

        return HttpResponseRedirect(f'/projects/{project_id}')
