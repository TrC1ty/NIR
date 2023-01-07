from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm, Material
from ..models.MaterialModel import MaterialModel
from app.models.WorkModel import WorkModel
from ..models.ParticipantModel import ParticipantModel
from app.forms.WorkForm import Work


class MaterialView(View):
    @staticmethod
    def get(request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm()
        participants = ParticipantModel.objects.filter(participant_type='SUP')

        return render(request, 'materials/creation.html', {'form': form, 'work_id': work_id,
                                                           'participants': participants})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        material = MaterialModel.objects.get(id=value)

        return render(request, 'materials/material.html', {'material': material})

    @staticmethod
    def post(request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm(request.POST)
        work = WorkModel.objects.get(id=work_id)
        if form.is_valid():
            name = form.cleaned_data['name']
            certificate = form.cleaned_data['certificate']
            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            provider_id = request.POST['provider']
            provider = ParticipantModel.objects.get(id=provider_id)
            new_material = MaterialModel.objects.create(
                name=name,
                certificate=certificate,
                date_start=date_start,
                date_end=date_end,
                provider=provider,
            )
            new_material.save()
            work.materials.add(new_material)
            work.save()

        form = Work(instance=work)

        return render(request, 'works/edit.html', {'work': work, 'form': form})

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        materials = MaterialModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})

    @staticmethod
    def edit(request: HttpRequest, value) -> HttpResponse:
        material = MaterialModel.objects.get(id=value)

        if request.method == 'POST':
            form = MaterialForm(request.POST)
            if form.is_valid():
                material.name = form.cleaned_data['name']
                material.certificate = form.cleaned_data['certificate']
                material.date_start = form.cleaned_data['date_start']
                material.date_end = form.cleaned_data['date_end']
                material.save()

        form = Material(instance=material)

        return render(request, 'materials/edit.html', {'material': material,
                                                       'form': form})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        material = MaterialModel.objects.get(id=value)
        material.delete()
        materials = MaterialModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})