from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm
from ..models.MaterialModel import MaterialModel


class MaterialView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = MaterialForm()

        return render(request, 'creation/material.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = MaterialForm(request.POST)
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
            )
            new_material.save()

            return HttpResponseRedirect('/')
