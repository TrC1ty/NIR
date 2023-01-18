from django.db import models


class ParticipantModel(models.Model):
    SubjectType = (
        ('ЮЛ', 'Юридическое лицо'),
        ('ФЛ', 'Физическое лицо'),
        ('ИП', 'Индивидуальный предприниматель'),
    )
    ParticipantType = (
        ('SUP', 'Поставщик'),
        ('DEV', 'Разработчик'),
        ('REP', 'Представитель'),
        ('OTH', 'Другое'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True)
    surname = models.TextField()
    name = models.TextField()
    patronymic = models.TextField()
    post = models.TextField()
    passport_data = models.TextField()
    register_of_specialists = models.IntegerField(blank=True, null=True)
    ogrn = models.TextField()
    inn = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    legal_name = models.TextField()
    details_admin_doc = models.TextField()
    sro_name = models.TextField(null=True)
    sro_inn = models.TextField(null=True)
    sro_ogrn = models.TextField(null=True)
    participant_type = models.CharField(
        max_length=3,
        choices=ParticipantType,
    )
    subject_type = models.CharField(
        max_length=2,
        choices=SubjectType,
    )

    class Meta:
        db_table = "Participants"
