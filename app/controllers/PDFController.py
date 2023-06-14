import json

from rest_framework.response import Response

from app.models.MaterialModel import MaterialModel
from app.models.LegalActModel import LegalActModel

from django.http import FileResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from app.models.PdfModel import PdfModel


class PDFController(APIView):
    @staticmethod
    @api_view(('GET',))
    def get_certificate(request, material_id):
        material = MaterialModel.objects.get(id=material_id)

        response = FileResponse(material.file_data)
        response['Content-Type'] = material.file_type

        return response

    @staticmethod
    @api_view(('GET',))
    def get_act(request, act_id):
        act = LegalActModel.objects.get(id=act_id)

        response = FileResponse(act.file_data)
        response['Content-Type'] = act.file_type

        return response

    @staticmethod
    @api_view(('POST',))
    def save_pdf(request):
        form = json.loads(request.body)
        pdf = PdfModel.objects.create(
            file_type=form['file_type'],
            file_data=bytearray(form['file_data']),
        )

        return Response({
            'src': f'/api/pdf/view/{pdf.id}',
            'id': pdf.id,
        })

    @staticmethod
    @api_view(('GET',))
    def view_pdf(request, pdf_id):
        pdf = PdfModel.objects.get(id=pdf_id)

        response = FileResponse(pdf.file_data)
        response['Content-Type'] = pdf.file_type

        return response

    @staticmethod
    @api_view(('DELETE',))
    def delete_pdf(request, pdf_id):
        pdf = PdfModel.objects.get(id=pdf_id)
        pdf.delete()

        return Response(status=status.HTTP_200_OK)
