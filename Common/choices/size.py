from django.db import models


class QualityChoice(models.IntegerChoices):
    SIZE144 = 10, "144p"
    SIZE240 = 20, "240p"
    SIZE360 = 30, "360p"
    SIZE480 = 40, "480p"
    SIZE720 = 50, "720p"
    SIZE1080 = 60, "1080p"
    SIZE1440 = 70, "1440p"
