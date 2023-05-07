from app.models.WorkModel import WorkModel
from django.db import models
from rest_framework import serializers


class BCARModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "BCARs"


class BcarSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField()
