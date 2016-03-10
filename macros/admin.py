from django.contrib import admin

from .models import UnicodeMacro


class UnicodeMacroAdmin(admin.ModelAdmin):
    list_display = ('safe_text', 'shortcut')

    class Media:
        css = {
                'all': ('admin/css/macros.css',)
        }

admin.site.register(UnicodeMacro, UnicodeMacroAdmin)
