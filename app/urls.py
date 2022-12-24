from django.urls import path
from app.views.HomeView import HomeView
from app.views.WorkView import WorkView
from app.views.MaterialView import MaterialView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-work', WorkView.as_view(), name='create-work'),
    path('create-material', MaterialView.as_view(), name='create-material'),
]
