# common/validators/phone_validator.py
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_valid = RegexValidator(
    regex=r"^\+998\d{9}$",
    message=_("Telefon raqam formati: +998901234567 bo'lishi kerak."),
)
