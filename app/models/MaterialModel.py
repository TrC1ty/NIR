from django.db import models
from .ParticipantModel import ParticipantModel


class MaterialModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    certificate = models.TextField()
    count = models.TextField(null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    provider = models.ForeignKey(ParticipantModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Materials"
