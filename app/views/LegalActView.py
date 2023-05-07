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

    @staticmethod
    def edit_acts(request: HttpRequest, work_id) -> HttpResponse:
        work = WorkModel.objects.get(id=work_id)
        actForm = request.POST.dict()
        actIds = re.findall(r'act\d+', ", ".join(actForm.keys()))
        acts = []
        for actId in actIds:
            elementId = re.search(r"\d+", actId).group()
            querySet = work.acts.filter(id=elementId)
            if querySet:
                act = querySet.get()
                act.name = actForm[actId]
                act.save()
                acts.append(act)
            else:
                act = LegalActModel.objects.create(
                    name=actForm[actId],
                )
                act.save()
                acts.append(act)

        for el in work.acts.all():
            if el not in acts:
                el.delete()

        work.acts.clear()
        work.acts.add(*acts)
        work.save()

        form = Work(instance=work)

        return render(request, 'works/View.html', {'work': work, 'form': form})
