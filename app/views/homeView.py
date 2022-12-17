from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render


class HomeView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        return render(request, 'home/home.html', {})
