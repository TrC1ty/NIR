from django.db import models
from django.utils.translation import gettext_lazy as _


class ParticipantType(models.TextChoices):
    SUPPLIER = 'SUP', _("Поставщик")
    DEVELOPER = 'DEV', _("Разработчик")
    REPRESENTATIVE = 'REP', _("Представитель")
    OTHER = 'OTH', _("Другое")


class SubjectType(models.TextChoices):
    LEGAL_ENTITY = 'ЮЛ', _("Юридическое лицо")
    NATURAL_PERSON = 'ФЛ', _("Физическое лицо")
    INDIVIDUAL_ENTREPRENEUR = 'ИП', _("Индивидуальный предприниматель")
    SELF_REGULATING_ORGANIZATION = 'СО', _("Саморегулируемая организация")
