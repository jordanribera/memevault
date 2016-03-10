from django.db import models
from django.utils.html import format_html

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

    def safe_text(self):
        return format_html(
            '<span class="emoji-safe">{}</span>',
            self.text
        )

    safe_text.short_description = 'Macro Text'
