from django.db import models

from Common.choices.size import QualityChoice


class Upload(models.Model):
    file = models.FileField(upload_to="uploads/", null=True)
    quality = models.PositiveIntegerField(choices=QualityChoice.choices, null=True, blank=True)

    def __str__(self):
        return f"Upload {self.id}"
