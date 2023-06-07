import json

from app.models.WorkModel import WorkModel
from app.models.MaterialModel import MaterialModel, MaterialSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class MaterialController(APIView):
    @staticmethod
    @api_view(('GET',))
    def get_by_filter(request):
        work_id = request.GET.get("work_id")
        if work_id:
            queryset = MaterialModel.objects.filter(work_id=work_id)
        else:
            project_id = request.GET.get("project_id")
            queryset = MaterialModel.objects.filter(work__projectSection__project_id=project_id)

        serializer_for_queryset = MaterialSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)

    @staticmethod
    @api_view(('POST',))
    def post(request, work_id):
        form = json.loads(request.body)
        work = WorkModel.objects.get(id=work_id)
        MaterialModel.objects.create(
            name=form['name'],
            count=form['count'],
            units_of_measurement=form['units_of_measurement'],
            list_count=form['list_count'],
            provider=form['provider'],
            certificate_name=form['certificate_name'],
            certificate_number=form['certificate_number'],
            date_start=form['date_start'],
            date_end=form['date_end'],
            file_name=form['file_name'],
            file_type=form['file_type'],
            file_data=bytearray(form['file_data']),
            work=work
        )

        queryset = MaterialModel.objects.filter(work=work)
        serializer_for_queryset = MaterialSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)
