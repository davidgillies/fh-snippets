from django.contrib import admin
from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('author', 'source_title', 'source_type')
    search_fields = ['author', 'source_title', 'snippet']

admin.site.register(Snippet, SnippetAdmin)
