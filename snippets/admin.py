from django.contrib import admin

from .models import Language, Snippet


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    # llenamos el campo Slug automaticamente
    prepopulated_fields = {'slug':('name',)}


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
