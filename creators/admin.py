from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Artist

class ImportExportAdmin(ImportExportModelAdmin, admin.ModelAdmin) :
    pass

admin.site.register(Artist, ImportExportAdmin)
