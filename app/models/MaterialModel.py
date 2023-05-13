from django.db import models
from rest_framework import serializers
from app.models.WorkModel import WorkModel


class MaterialModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    count = models.TextField(null=True)
    units_of_measurement = models.TextField(null=True)
    list_count = models.TextField(null=True)
    provider = models.TextField()
    certificate_name = models.TextField()
    certificate_number = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    file_name = models.TextField()
    file_type = models.TextField()
    file_data = models.BinaryField()
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Materials"


class MaterialSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    name = serializers.CharField()
    count = serializers.CharField()
    units_of_measurement = serializers.CharField()
    date_end = serializers.DateField()
