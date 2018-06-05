from django.contrib import admin

from .models import *

admin.site.site_header = 'Admin Interface'

admin.site.register(User)
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
