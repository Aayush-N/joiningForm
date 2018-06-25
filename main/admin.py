from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


from .models import *

admin.site.site_header = 'Admin Interface'

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	list_display = ('username', 'first_name', 'email', 'declared')
	search_fields = ('username','email', 'first_name','phone')
	list_filter = ('declared',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	search_fields = ('Applicant__username', 'Applicant__email')
	list_display = ('Applicant', 'Degree')
	list_filter = ('Applicant__declared',)

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'Spec_awards_particulars', 'state', 'national', 'international')
	list_filter = ('faculty__declared',)

@admin.register(Proficiency)
class ProficiencyAdmin(admin.ModelAdmin):
	pass

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
	pass

@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'signature',)
	list_filter = ('faculty__declared',)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'name', 'position', 'designation', 'affiliation')
	list_filter = ('faculty__declared',)

@admin.register(IndustrialExperience)
class IndustrialExperienceAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'organisation', 'experience_years', )
	list_filter = ('faculty__declared',)

@admin.register(TeachingExperience)
class TeachingExperienceAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'university_name', 'designation', )
	list_filter = ('faculty__declared',)

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'university_name', 'area_reasearch', 'total_duration')
	list_filter = ('faculty__declared',)

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'conf_conducted_org', 'university', 'total_duration',)
	list_filter = ('faculty__declared',)

@admin.register(SpecialAchievement)
class SpecialAchievementAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'community_service', 'industry_related', 'university_assignment','administration')
	list_filter = ('faculty__declared',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	search_fields = ('faculty__username', 'faculty__email')
	list_display = ('faculty', 'type_of_member', 'professional_body', 'annual',)
	list_filter = ('faculty__declared',)

