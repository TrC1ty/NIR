import re
from pathlib import Path

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.encoding import escape_uri_path
from docxtpl import DocxTemplate

from app.models.LegalActModel import LegalActModel
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from ..forms.WorkForm import WorkForm, Work


class LegalActView(View):
    @staticmethod
    def view_act(request: HttpRequest, act_id):
        legalAct = LegalActModel.objects.get(id=act_id)

        response = HttpResponse(legalAct.file_data)
        response['Content-Type'] = legalAct.file_type
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(legalAct.file_name)

        return response
