from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from .models import *

admin.site.site_header = 'Admin Interface'

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Proficiency)
admin.site.register(Degree)
admin.site.register(Course)

admin.site.register(Declaration)
admin.site.register(DocumentUpload)
admin.site.register(DocumentType)
admin.site.register(Referral)
admin.site.register(Awards)
admin.site.register(IndustrialExperience)
admin.site.register(TeachingExperience)
admin.site.register(Research)
admin.site.register(Conference)
