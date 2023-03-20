from django.db import models


class ParticipantModel(models.Model):
    SubjectType = (
        ('ЮЛ', 'Юридическое лицо'),
        ('ФЛ', 'Физическое лицо'),
        ('ИП', 'Индивидуальный предприниматель'),
    )
    ParticipantType = (
        ('SUP', 'Поставщик'),
        ('CONSTR', 'Участник строительства'),
        ('REP', 'Представитель'),
        ('OTH', 'Другое'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True)
    surname = models.TextField()
    name = models.TextField()
    patronymic = models.TextField()
    post = models.TextField()
    passport_data = models.TextField()
    register_of_specialists = models.TextField(null=True)
    ogrn = models.TextField()
    inn = models.TextField()
    kpp = models.TextField(null=True)
    bic = models.TextField(null=True)
    payment_account = models.TextField(null=True)
    cor_account = models.TextField(null=True)
    okpo = models.TextField(null=True)
    okato = models.TextField(null=True)
    okved = models.TextField(null=True)
    mail = models.TextField(null=True)
    site = models.TextField(null=True)
    address = models.TextField()
    post_address = models.TextField(null=True)
    phone = models.TextField()
    legal_name = models.TextField()
    details_admin_doc = models.TextField()
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
