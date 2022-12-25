import enum

from django.db import models
from django.forms.models import model_to_dict


class ParticipantModel(models.Model):
    @enum.unique
    class ParticipantType(models.TextChoices):
        SUPPLIER = 1
        DEVELOPER = 2
        REPRESENTATIVE = 3
        OTHER = 4

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]

    @enum.unique
    class SubjectType(models.TextChoices):
        LEGAL_ENTITY = 1
        NATURAL_PERSON = 2
        INDIVIDUAL_ENTREPRENEUR = 3

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]

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
    participant_type = models.CharField(max_length=255, choices=ParticipantType.choices(),
                                        default=ParticipantType.OTHER)
    subject_type = models.CharField(max_length=255, choices=SubjectType.choices(), default=SubjectType.NATURAL_PERSON)

    class Meta:
        db_table = "Participants"
