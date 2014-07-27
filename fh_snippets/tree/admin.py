from django.contrib import admin
from tree.models import Tree, Family
# Register your models here.

class TreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tree, TreeAdmin)

class FamilyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Family, admin.ModelAdmin)

