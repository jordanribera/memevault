from django.db import models

from memecore.models import Tag


class UnicodeMacro(models.Model):
    shortcut = models.CharField(
        max_length=64,
        unique=True
    )

    text = models.CharField(
        max_length=255
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='unicode_macros',
        blank=True
    )

    def __str__(self):
        return self.text
