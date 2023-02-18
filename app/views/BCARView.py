import re
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.BCARForm import BCARForm
from app.models.BCARModel import BCARModel
from ..models.MaterialModel import MaterialModel
from ..models.WorkModel import WorkModel
from app.forms.WorkForm import Work, WorkForm


class BCARView(View):
    @staticmethod
    def get(request: HttpRequest, work_id) -> HttpResponse:
        form = BCARForm()

        return render(request, 'bcars/creation.html', {'form': form, 'work_id': work_id})

    @staticmethod
    def post(request: HttpRequest, work_id) -> HttpResponse:
        work = WorkModel.objects.get(id=work_id)
        bcarForm = request.POST.dict()
        bcarIds = re.findall(r'bcar\d+', ", ".join(bcarForm.keys()))
        bcars = []
        for bcarId in bcarIds:
            elementId = re.search(r"\d+", bcarId).group()
            querySet = work.bcars.filter(id=elementId)
            if querySet:
                bcar = querySet.get()
                bcar.name = bcarForm[bcarId]
                bcar.save()
                bcars.append(bcar)
            else:
                bcar = BCARModel.objects.create(
                    name=bcarForm[bcarId],
                )
                bcar.save()
                bcars.append(bcar)

        for el in work.bcars.all():
            if el not in bcars:
                el.delete()

        work.bcars.clear()
        work.bcars.add(*bcars)
        work.save()

        form = Work(instance=work)

        return render(request, 'works/edit.html', {'work': work, 'form': form})

    @staticmethod
    def delete(request: HttpRequest, work_id, bcar_id) -> HttpResponse:
        bcar = BCARModel.objects.get(id=bcar_id)
        work = WorkModel.objects.get(id=work_id)
        bcar.delete()

        return HttpResponseRedirect(f'/works/edit/{work.id}')
