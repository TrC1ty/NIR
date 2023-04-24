import json

from app.models.ProjectSection import ProjectSectionSerializer
from app.models.ProjectSection import ProjectSection
from app.models.ProjectModel import ProjectModel
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
        serializer_for_queryset = ProjectSectionSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)
