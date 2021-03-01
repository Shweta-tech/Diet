from django.contrib import admin
from registration.models import User,ProjectManager
from resources.models import Document
from import_export.admin import ImportExportModelAdmin
# # Register your models here.

admin.site.register(ProjectManager)
admin.site.register(Document)
class bulkAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','username','email', 'password1', 'password2','contact')


