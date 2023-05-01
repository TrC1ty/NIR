from django.db import models
from rest_framework import serializers
from app.models.WorkModel import WorkModel


class MaterialModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    certificate = models.TextField()
    count = models.TextField(null=True)
    units_of_measurement = models.TextField(null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    provider = models.TextField()
    list_count = models.TextField(null=True)
    # certificate_content = models.BinaryField()
    # certificate_name = models.TextField()
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Materials"


class MaterialSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField()
    count = serializers.CharField()
    units_of_measurement = serializers.CharField()
    date_end = serializers.DateField()
