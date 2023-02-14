from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.BCARForm import BCARForm
from app.models.BCARModel import BCARModel
from ..models.WorkModel import WorkModel
from app.forms.WorkForm import Work


class BCARView(View):
    @staticmethod
    def get(request: HttpRequest, work_id) -> HttpResponse:
        form = BCARForm()

        return render(request, 'bcars/creation.html', {'form': form, 'work_id': work_id})

    @staticmethod
    def post(request: HttpRequest, work_id) -> HttpResponse:
        work = WorkModel.objects.get(id=work_id)
        form = BCARForm(request.POST)
        if form.is_valid():
            bcar = BCARModel.objects.create(
                code_of_rules_number=form.cleaned_data["code_of_rules_number"],
                name=form.cleaned_data["name"],
            )
            bcar.save()
            work.bcars.add(bcar)
            work.save()

        form = Work(instance=work)

        return render(request, 'works/edit.html', {'work': work, 'form': form})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        bcar = BCARModel.objects.get(id=value)
        bcar.delete()
        materials = BCARModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})
