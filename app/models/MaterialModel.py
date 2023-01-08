from django.db import models
from .ParticipantModel import ParticipantModel

from .BCARModel import BCARModel


class MaterialModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    certificate = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    provider = models.ForeignKey(ParticipantModel, on_delete=models.CASCADE)
    bcars = models.ManyToManyField(BCARModel)

    class Meta:
        db_table = "Materials"
