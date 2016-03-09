from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    exclude = ('emoji_glyphs', 'unicode_macros')

admin.site.register(Tag, TagAdmin)
