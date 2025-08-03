from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from Common.models import BaseModel
from Common.validators import phone_validator,passport_validator
from Common.choices.role import RoleChoice
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone = models.CharField(
        verbose_name=_("phone number"),
        max_length=15,
        unique=True,
        db_index=True,
        validators=[phone_validator.phone_valid],
        help_text=_("Masalan: +998901234567"),
    )
    passport_series = models.CharField(
        verbose_name=_("Passport series"),
        max_length=9,
        unique=True,
        help_text=_("Masalan: AA1234567"),
        validators=[passport_validator.passport_valid],
        blank=True,
        null=True,
        # db_index=True, # uniq ishlatilgani uchun kerak emas
    )
    first_name = models.CharField(
        verbose_name=_("Frist name"),
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=25,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
    )
    role = models.IntegerField(
        choices=RoleChoice.choices,
        default=RoleChoice.USER,  # oddiy user yani xaridor bo'lib kirish uchun
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting user."
        ),
        verbose_name=_("active"),
    )

    is_staff = models.BooleanField(
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
        verbose_name=_("staff status"),
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_("superuser status"),
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("date joined"),
    )
    objects = UserManager()

    USERNAME_FIELD = "phone"

    class Meta:
        ordering = ("-id",)
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.phone
