from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def normalize_phone(self, phone: str) -> str:
        phone = phone.strip().replace(" ", "").replace("-", "")
        if phone.startswith("998"):
            phone = "+" + phone
        elif phone.startswith("9"):
            phone = "+998" + phone
        return phone

    def _create_user(self, phone: str, password: str = None, **extra_fields):
        """Foydalanuvchini yaratishning umumiy metodi (ichki)."""
        if not phone:
            raise ValueError("Telefon raqam bo'lishi shart.")

        email = extra_fields.get("email")
        if email:
            extra_fields["email"] = self.normalize_email(email)

        phone = self.normalize_phone(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone: str, password: str = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser is_staff=True bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser is_superuser=True bo'lishi kerak.")

        return self._create_user(phone, password, **extra_fields)
