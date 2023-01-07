from django.db import models
from .ParticipantModel import ParticipantModel

from .BCARModel import BCARModel


class MaterialModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    certificate = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    provider = models.ForeignKey(ParticipantModel, on_delete=models.CASCADE)
    bcar = models.ForeignKey(BCARModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Materials"
