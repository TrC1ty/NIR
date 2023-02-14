import re
from pathlib import Path

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from docxtpl import DocxTemplate

from app.models.LegalActModel import LegalActModel
from app.models.ProjectModel import ProjectModel
from app.models.WorkModel import WorkModel
from ..forms.WorkForm import WorkForm, Work

class LegalActView(View):
    @staticmethod
    def editacts(request: HttpRequest, value) -> HttpResponse:
        work = WorkModel.objects.get(id=value)

        if request.method == 'POST':
            print(request.POST)

            actForm = request.POST.dict()
            print(f"!!!!!!!!!!!!!!{actForm}!!!!!!!!!!!")
            actNames = re.findall(r'act\d+', ", ".join(actForm.keys()))
            print(f"!!!!!!!!!!!!!!{actNames}!!!!!!!!!!!")
            acts = []
            for actName in actNames:
                act = LegalActModel.objects.create(
                    name=actForm[actName],
                )
                act.save()
                acts.append(act)

            work.acts.clear()
            work.acts.add(*acts)
            work.save()

        form = Work(instance=work)

        return render(request, 'works/edit.html', {'work': work,
                                                   'form': form})
