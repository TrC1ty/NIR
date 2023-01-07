from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.BCARForm import BCARForm
from app.models.BCARModel import BCARModel
from ..models.MaterialModel import MaterialModel
from app.forms.MaterialForm import Material


class BCARView(View):
    @staticmethod
    def get(request: HttpRequest, material_id) -> HttpResponse:
        form = BCARForm()

        return render(request, 'bcars/creation.html', {'form': form, 'material_id': material_id})

    @staticmethod
    def post(request: HttpRequest, material_id) -> HttpResponse:
        material = MaterialModel.objects.get(id=material_id)
        form = BCARForm(request.POST)
        if form.is_valid():
            bcar = BCARModel.objects.create(
                code_of_rules_number=form.cleaned_data["code_of_rules_number"],
                name=form.cleaned_data["name"],
            )
            bcar.save()
            material.bcars.add(bcar)
            material.save()

        form = Material(instance=material)

        return render(request, 'materials/edit.html', {'material': material, 'form': form})
