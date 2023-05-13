from django.http import HttpRequest, HttpResponse
from django.views import View
from django.utils.encoding import escape_uri_path

from ..models.MaterialModel import MaterialModel


class MaterialView(View):
    @staticmethod
    def view_certificate(request: HttpRequest, material_id):
        material = MaterialModel.objects.get(id=material_id)

        response = HttpResponse(material.file_data)
        response['Content-Type'] = material.file_type
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(material.file_name)

        return response
