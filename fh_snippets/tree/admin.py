from django.contrib import admin
from tree.models import Tree, Family
# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'birth_date')

admin.site.register(Tree, TreeAdmin)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('husband', 'wife', 'marriage_date')

admin.site.register(Family, FamilyAdmin)

