import enum
from enum import Enum
from enumchoicefield import EnumChoiceField
from django.db import models


class ParticipantModel(models.Model):
    @enum.unique
    class ParticipantType(Enum):
        SUPPLIER = 1
        DEVELOPER = 2
        REPRESENTATIVE = 3
        OTHER = 4

    @enum.unique
    class SubjectType(Enum):
        LEGAL_ENTITY = 1
        NATURAL_PERSON = 2
        INDIVIDUAL_ENTREPRENEUR = 3

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
    participant_type = EnumChoiceField(
        ParticipantType,
        default=ParticipantType.OTHER
    )
    subject_type = EnumChoiceField(
        SubjectType,
        default=SubjectType.NATURAL_PERSON
    )

    class Meta:
        db_table = "Participants"
