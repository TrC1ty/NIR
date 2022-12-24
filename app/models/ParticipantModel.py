from django.db import models
from django.forms.models import model_to_dict


class ParticipantModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    surname = models.TextField()
    name = models.TextField()
    patronymic = models.TextField()
    post = models.TextField()
    passport_data = models.TextField()
    register_of_specialists = models.IntegerField()
    ogrn = models.IntegerField()
    inn = models.IntegerField()
    address = models.TextField()
    phone = models.TextField()
    legal_name = models.TextField()
    details_admin_doc = models.TextField()

    class Meta:
        db_table = "participant_model"
