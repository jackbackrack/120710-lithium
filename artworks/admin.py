from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Artwork

class ImportExportAdmin(ImportExportModelAdmin, admin.ModelAdmin) :
    pass

admin.site.register(Artwork, ImportExportAdmin)


