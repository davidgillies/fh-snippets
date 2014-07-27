from django.contrib import admin
from biogs.models import Biog
# Register your models here.

class BiogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Biog, BiogAdmin)
