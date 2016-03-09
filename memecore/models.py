from django.db import models


class Tag(models.Model):
    slug = models.SlugField(
        allow_unicode=True,
        unique=True
    )

    def __str__(self):
        return self.slug
