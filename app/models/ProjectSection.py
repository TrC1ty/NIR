from django.db import models
from .ProjectModel import ProjectModel
from rest_framework import serializers


class ProjectSection(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        db_table = "ProjectSection"


class ProjectSectionSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    name = serializers.CharField()
    count = serializers.IntegerField()
