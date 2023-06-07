import json

from app.models.ProjectSection import ProjectSectionSerializer
from app.models.ProjectSection import ProjectSection
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ProjectSectionModel:
    def __init__(self, object_id, name, count):
        self.id = object_id
        self.name = name
        self.count = count


class ProjectSectionController(APIView):
    @staticmethod
    @api_view(('POST',))
    def post(request: HttpRequest, project_id):
        form = json.loads(request.body)
        project = ProjectModel.objects.get(id=project_id)
        ProjectSection.objects.create(
            project=project,
            name=form['section_name']
        )

        queryset = ProjectSection.objects.filter(project=project)
        sections = []
        for section in queryset:
            count = WorkModel.objects.filter(projectSection__id=section.id).count()
            sections.append(ProjectSectionModel(section.id, section.name, count))

        serializer_for_queryset = ProjectSectionSerializer(
            instance=sections,
            many=True
        )

        return Response(serializer_for_queryset.data)

    @staticmethod
    @api_view(('DELETE',))
    def delete(request: HttpRequest, section_id):
        project_section = ProjectSection.objects.get(id=section_id)
        project_id = project_section.project_id
        project_section.delete()

        queryset = ProjectSection.objects.filter(project_id=project_id)
        sections = []
        for section in queryset:
            count = WorkModel.objects.filter(projectSection__id=section.id).count()
            sections.append(ProjectSectionModel(section.id, section.name, count))

        serializer_for_queryset = ProjectSectionSerializer(
            instance=sections,
            many=True
        )

        return Response(serializer_for_queryset.data)
