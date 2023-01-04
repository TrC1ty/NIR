from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from ..models.ParticipantModel import ParticipantModel
from ..forms.ParticipantForm import ParticipantForm


class ParticipantView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        participants = ParticipantModel.objects.all()

        return render(request, 'participants/index.html', {'participants': participants})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            return render(request, 'participants/creation.html', {'form': form})
