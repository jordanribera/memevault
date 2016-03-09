from django.contrib import admin
from django import forms

from .models import EmojiGlyph


class EmojiGlyphForm(forms.ModelForm):
    class Meta:
        model = EmojiGlyph
        fields = ['character']

    def clean_character(self):
        character = self.cleaned_data.get('character')
        if len(character) > 1:
            raise forms.ValidationError('Too many characters.')

        return character


class EmojiGlyphAdmin(admin.ModelAdmin):
    form = EmojiGlyphForm


admin.site.register(EmojiGlyph, EmojiGlyphAdmin)
