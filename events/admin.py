from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Event, Show

class ImportExportAdmin(ImportExportModelAdmin, admin.ModelAdmin) :
    pass

admin.site.register(Event, ImportExportAdmin)
admin.site.register(Show, ImportExportAdmin)

