from django.core.mail.backends import console
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm, Material
from ..forms.ParticipantForm import ParticipantForm, Participant
from ..models.MaterialModel import MaterialModel
from app.models.WorkModel import WorkModel
from ..models.ParticipantModel import ParticipantModel
from app.forms.WorkForm import Work


class MaterialView(View):
    @staticmethod
    def get(request: HttpRequest, work_id) -> HttpResponse:
        form_material = MaterialForm()
        participants = ParticipantModel.objects.filter(participant_type='SUP')

        return render(request, 'materials/creation.html', {'form_material': form_material, 'work_id': work_id,
                                                           'participants': participants})

    @staticmethod
    def view(request: HttpRequest, value) -> HttpResponse:
        material = MaterialModel.objects.get(id=value)

        return render(request, 'materials/material.html', {'material': material})

    @staticmethod
    def post(request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm(request.POST)
        work = WorkModel.objects.get(id=work_id)
        participants = ParticipantModel.objects.filter(participant_type='SUP')
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            certificate = form.cleaned_data['certificate']
            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            count = form.cleaned_data['count']
            list_count = form.cleaned_data['list_count']
            if request.POST.get("participant") is not None:
                provider = ParticipantModel.objects.create(
                    participant_type="SUP",
                    subject_type="ЮЛ",
                    legal_name=request.POST.get("participant"),
                )
                provider.save()
            else:
                provider_id = request.POST['provider']
                provider = ParticipantModel.objects.get(id=provider_id)

            new_material = MaterialModel.objects.create(
                name=name,
                certificate=certificate,
                date_start=date_start,
                date_end=date_end,
                provider=provider,
                count=count,
                list_count=list_count
            )
            new_material.save()
            work.materials.add(new_material)
            work.save()

            form = Work(instance=work)

            return render(request, 'works/edit.html', {'work': work, 'form': form})

        return render(request, 'materials/creation.html', {'form_material': form, 'work_id': work_id,
                                                           'participants': participants})



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
                material.count = form.cleaned_data['count']
                material.list_count = form.cleaned_data['list_count']
                material.save()

                return render(request, 'materials/material.html', {'material': material})

        form = Material(instance=material)

        return render(request, 'materials/edit.html', {'material': material,
                                                       'form': form})

    @staticmethod
    def delete(request: HttpRequest, value) -> HttpResponse:
        material = MaterialModel.objects.get(id=value)
        material.delete()
        materials = MaterialModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})