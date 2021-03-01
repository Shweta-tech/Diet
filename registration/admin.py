
# Register your models here.
from django.contrib import admin
from .models import User,SchoolCoordinator
# from resources.models import Document
from import_export.admin import ImportExportModelAdmin
# # Register your models here.

admin.site.register(SchoolCoordinator)
# admin.site.register(Document)
class bulkAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','username','email', 'password1', 'password2','contact','schoolname','personaladdress')