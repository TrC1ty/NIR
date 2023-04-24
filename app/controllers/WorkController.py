from app.models.WorkModel import WorkModel, WorkSerializer
from app.models.ProjectSection import ProjectSection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class WorkController(APIView):
    @staticmethod
    @api_view(('GET',))
    def get(request, project_section_id):
        project_section = ProjectSection.objects.get(id=project_section_id)
        queryset = WorkModel.objects.filter(projectSection=project_section)
        serializer_for_queryset = WorkSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)
