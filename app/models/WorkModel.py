from django.db import models
from .BCARModel import BCARModel
from .ProjectSection import ProjectSection
from .MaterialModel import MaterialModel
from .LegalActModel import LegalActModel
from rest_framework import serializers


class WorkModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name_hidden_works = models.TextField()
    number_project_doc = models.TextField()
    number_working_doc = models.TextField(null=True)
    other_details_project_drawing = models.TextField(null=True)
    other_details_working_drawing = models.TextField(null=True)
    name_project_doc = models.TextField(null=True)
    name_working_doc = models.TextField(null=True)
    information_persons_prepare_doc = models.TextField(null=True)
    start_date_work = models.DateField()
    end_date_work = models.DateField()
    permitted_works = models.TextField(null=True)
    additional_information = models.TextField(null=True)
    number_instances = models.IntegerField(default=0, null=True)
    materials = models.ManyToManyField(MaterialModel)
    bcars = models.ManyToManyField(BCARModel)
    acts = models.ManyToManyField(LegalActModel)

    projectSection = models.ForeignKey(ProjectSection, on_delete=models.CASCADE)

    class Meta:
        db_table = "Works"


class WorkSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    name_hidden_works = serializers.CharField()
    end_date_work = serializers.DateField()
