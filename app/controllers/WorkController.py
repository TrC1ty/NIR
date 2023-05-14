import json

from app.models.BCARModel import BCARModel, BcarSerializer
from app.models.WorkModel import WorkModel, WorkSerializer
from app.models.ProjectSection import ProjectSection
from app.models.LegalActModel import LegalActModel, LegalActSerializer

from django.http import HttpRequest

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

    @staticmethod
    @api_view(('POST',))
    def create_bcar(request: HttpRequest, work_id):
        form = json.loads(request.body)
        work = WorkModel.objects.get(id=work_id)
        BCARModel.objects.create(
            name=form['bcar_name'],
            work=work
        )

        queryset = BCARModel.objects.filter(work=work)
        serializer_for_queryset = BcarSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)

    @staticmethod
    @api_view(('POST',))
    def create_act(request: HttpRequest, work_id):
        form = json.loads(request.body)
        work = WorkModel.objects.get(id=work_id)

        LegalActModel.objects.create(
            name=form['name'],
            document_number=form['document_number'],
            document_date=form['document_date'],
            list_count=form['list_count'],
            file_name=form['act_name'],
            file_type=form['act_type'],
            file_data=bytearray(form['act_data']),
            work=work
        )

        queryset = LegalActModel.objects.filter(work=work)
        serializer_for_queryset = LegalActSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)
