from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..forms.MaterialForm import MaterialForm


class MaterialView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = MaterialForm()
        return render(request, 'creation/material.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = MaterialForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
