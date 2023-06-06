from app.models.MaterialModel import MaterialModel

from django.http import HttpResponse, FileResponse
from django.utils.encoding import escape_uri_path

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class PDFController(APIView):
    @staticmethod
    @api_view(('GET',))
    def get_certificate(request, material_id):
        material = MaterialModel.objects.get(id=material_id)

        response = FileResponse(material.file_data)
        response['Content-Type'] = material.file_type
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(material.file_name)

        return response
