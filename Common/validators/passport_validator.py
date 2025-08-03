# common/validators/passport_validator.py
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

passport_valid = RegexValidator(
    regex=r"^[A-Z]{2}\d{7}$",
    message=_("Passport seriya formati noto‘g‘ri. Masalan: AA1234567 bo‘lishi kerak."),
)
