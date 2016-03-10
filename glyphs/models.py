from django.db import models

from memecore.models import Tag


class EmojiGlyph(models.Model):
    character = models.CharField(
        max_length=16,
        unique=True
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='emoji_glyphs',
        blank=True
    )

    def __str__(self):
        return self.character
