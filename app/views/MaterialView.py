from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm
from ..models.MaterialModel import MaterialModel
from app.models.WorkModel import WorkModel


class MaterialView(View):
    def get(self, request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm()

        return render(request, 'materials/creation.html', {'form': form, 'work_id': work_id})

    def post(self, request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm(request.POST)
        work = WorkModel.objects.get(id=work_id)
        if form.is_valid():
            name = form.cleaned_data['name']
            certificate = form.cleaned_data['certificate']
            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            new_material = MaterialModel.objects.create(
                name=name,
                certificate=certificate,
                date_start=date_start,
                date_end=date_end,
                # works=work,
            )
            new_material.save()

            return HttpResponseRedirect('index')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        materials = MaterialModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})
