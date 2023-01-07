from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm
from ..models.MaterialModel import MaterialModel
from app.models.WorkModel import WorkModel
from ..models.ParticipantModel import ParticipantModel


class MaterialView(View):
    @staticmethod
    def get(request: HttpRequest, work_id) -> HttpResponse:
        form = MaterialForm()
        participants = ParticipantModel.objects.filter(participant_type='SUP')

        return render(request, 'materials/creation.html', {'form': form, 'work_id': work_id,
                                                           'participants': participants})

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
            print(provider)
            new_material = MaterialModel.objects.create(
                name=name,
                certificate=certificate,
                date_start=date_start,
                date_end=date_end,
                provider=provider,
            )
            new_material.save()
            new_material.works.add(work)
            new_material.save()

            return HttpResponseRedirect('/materials/index')

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse:
        materials = MaterialModel.objects.all()

        return render(request, 'materials/index.html', {'materials': materials})
