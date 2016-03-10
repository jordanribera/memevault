from django.contrib import admin

from .models import UnicodeMacro


class UnicodeMacroAdmin(admin.ModelAdmin):
    list_display = ('safe_text',)

admin.site.register(UnicodeMacro, UnicodeMacroAdmin)
