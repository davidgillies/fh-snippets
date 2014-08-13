from django.contrib import admin
from tree.models import Tree, Family
# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')

admin.site.register(Tree, TreeAdmin)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('husband', 'wife', 'marriage_date')
    search_fields = ['husband__first_name', 'husband__surname', 'wife__first_name', 'wife__surname', 'marriage_date']

admin.site.register(Family, FamilyAdmin)

