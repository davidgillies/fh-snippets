from django.contrib import admin
from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('tagname', 'tag_type', 'description')
    search_fields = ['tagname']

admin.site.register(Tag, TagAdmin)
