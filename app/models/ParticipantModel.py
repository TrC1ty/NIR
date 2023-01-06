from django.db import models
from app.models.Enums import ParticipantType, SubjectType


class ParticipantModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    surname = models.TextField()
    name = models.TextField()
    patronymic = models.TextField()
    post = models.TextField()
    passport_data = models.TextField()
    register_of_specialists = models.IntegerField()
    ogrn = models.TextField()
    inn = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    legal_name = models.TextField()
    details_admin_doc = models.TextField()
    participant_type = models.CharField(
        max_length=3,
        choices=ParticipantType.choices,
        default=ParticipantType.OTHER,
    )
    subject_type = models.CharField(
        max_length=2,
        choices=SubjectType.choices,
        default=SubjectType.NATURAL_PERSON,
    )

    class Meta:
        db_table = "Participants"
