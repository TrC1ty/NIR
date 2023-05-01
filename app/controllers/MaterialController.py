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
        queryset = MaterialModel.objects.filter(work_id=work_id)
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
            certificate=form['certificate'],
            date_start=form['date_start'],
            date_end=form['date_end'],
            provider='',
            count=form['count'],
            units_of_measurement=form['units_of_measurement'],
            list_count=form['list_count'],
            work=work
        )

        queryset = MaterialModel.objects.filter(work=work)
        serializer_for_queryset = MaterialSerializer(
            instance=queryset,
            many=True
        )

        return Response(serializer_for_queryset.data)
