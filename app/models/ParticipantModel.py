from django.db import models


class ParticipantModel(models.Model):
    SubjectType = (
        ('ЮЛ', 'Юридическое лицо'),
        ('ФЛ', 'Физическое лицо'),
        ('ИП', 'Индивидуальный предприниматель'),
    )
    ParticipantType = (
        ('CONSTR', 'Участник строительства'),
        ('REP', 'Представитель'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True)
    surname = models.TextField(null=True)
    name = models.TextField(null=True)
    patronymic = models.TextField(null=True)
    post = models.TextField(null=True)
    passport_data = models.TextField(null=True)
    register_of_specialists = models.TextField(null=True)
    ogrn = models.TextField(null=True)
    inn = models.TextField(null=True)
    kpp = models.TextField(null=True)
    bic = models.TextField(null=True)
    payment_account = models.TextField(null=True)
    cor_account = models.TextField(null=True)
    okpo = models.TextField(null=True)
    okato = models.TextField(null=True)
    okved = models.TextField(null=True)
    mail = models.TextField(null=True)
    site = models.TextField(null=True)
    address = models.TextField(null=True)
    post_address = models.TextField(null=True)
    phone = models.TextField(null=True)
    legal_name = models.TextField(null=True)
    short_name = models.TextField(null=True)
    details_admin_doc = models.TextField(null=True)
    sro_name = models.TextField(null=True)
    sro_inn = models.TextField(null=True)
    sro_ogrn = models.TextField(null=True)
    bank_name = models.TextField(null=True)
    taxation_system = models.TextField(null=True)
    general_manager = models.TextField(null=True)
    participant_type = models.CharField(
        max_length=6,
        choices=ParticipantType,
    )
    subject_type = models.CharField(
        max_length=2,
        choices=SubjectType,
    )

    class Meta:
        db_table = "Participants"
