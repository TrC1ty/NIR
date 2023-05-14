from django.db import models
from app.models.WorkModel import WorkModel
from rest_framework import serializers


class LegalActModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    document_number = models.TextField()
    document_date = models.DateField()
    list_count = models.TextField()
    file_name = models.TextField()
    file_type = models.TextField()
    file_data = models.BinaryField()
    work = models.ForeignKey(WorkModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "LegalActs"


class LegalActSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    name = serializers.CharField()
