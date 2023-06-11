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
from ..forms.LegalActForm import LegalAct
from ..forms.WorkForm import WorkForm, Work


class LegalActView(View):
    @staticmethod
    def view_act(request: HttpRequest, act_id):
        legalAct = LegalActModel.objects.get(id=act_id)

        response = HttpResponse(legalAct.file_data)
        response['Content-Type'] = legalAct.file_type
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(legalAct.file_name)

        return response

    @staticmethod
    def edit_legal_act(request: HttpRequest, act_id):
        legal_act = LegalActModel.objects.get(id=act_id)
        work_id = legal_act.work_id
        if request.method == "POST":
            form = LegalAct(request.POST)
            if form.is_valid():
                legal_act.name = form.cleaned_data.get('name')
                legal_act.document_number = form.cleaned_data.get('document_number')
                legal_act.document_date = form.cleaned_data.get('document_date')
                legal_act.list_count = form.cleaned_data.get('list_count')
                
                legal_act.save()
        else:
            form = LegalAct(instance=legal_act)

        data = {
            'work_id': work_id,
            'form': form,
            'act_id': act_id
        }

        return render(request, 'legalActs/Edit.html', data)

    @staticmethod
    def delete_legal_act(request: HttpRequest, act_id):
        legal_act = LegalActModel.objects.get(id=act_id)
        work_id = legal_act.work_id
        legal_act.delete()

        return HttpResponseRedirect(f'/works/{work_id}')
