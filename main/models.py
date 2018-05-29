from django.db import models

# Create your models here.

class FacultyForm(models.Model):
	position = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	fathers_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	permanent_address = models.CharField(max_length=50)
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	email = models.EmailField('email address', unique=False)
	date_of_birth = models.CharField(max_length=50)
	age = models.CharField(max_length=50)
	place = models.CharField(max_length=50)
	religion = models.CharField(max_length=50)
	reservation = models.CharField(max_length=50)
	family_members = models.IntegerField()

class Languages(models.Model):
	to_read
languages_known
to_read
to_speak
to_write
languages_known1
to_read1
to_speak1
to_write1
languages_known2
to_read2
to_speak2
to_write2
qualifications
PhD_Course
PhD_Specialisation
PhD_Institution_Name
PhD_Passing_Year
PhD_Percent_Marks
PhD_Class_Awarded
ME_Mtech_Course
ME_Mtech_Specialisation
ME_Mtech_Institution_Name
ME_Mtech_Passing_Year
ME_Mtech_Percent_Marks
ME_Mtech_Class_Awarded
Mphil_mca_Course
Mphil_mca_Specialisation
Mphil_mca_Institution_Name
Mphil_mca_Passing_Year
Mphil_mca_Percent_Marks
Mphil_mca_Class_Awarded
BE_Btech_Course
BE_Btech_Specialisation
BE_Btech_Institution_Name
BE_Btech_Passing_Year
BE_Btech_Percent_Marks
BE_Btech_Class_Awarded
Bsc_Course
Bsc_Specialisation
Bsc_Institution_Name
Bsc_Passing_Year
Bsc_Percent_Marks
Bsc_Class_Awarded
others_Course
others_Specialisation
others_Institution_Name
others_Passing_Year
others_Percent_Marks
others_Class_Awarded
total_researchExp
Name_university
area_reasearch
research_from
research_to
research_total
total_internationalConf
title_paper
conf_International
year_month_pub
conf_conducted_org
teaching_totalExp
teaching_university
teaching_designation
teaching_from
teaching_to
teaching_total
total_industrialExp
industrial_org
industrial_positionheld
industrial_from
industrial_to
industrial_total
Affiliation_profbody
Affiliation_grade
Affiliation_no_member
Affiliation_year_selection
Spec_awards_particulars
awards_state
awards_national
awards_intnational
ref_name
ref_position
ref_add_contactNo
neft
uti
Date
Amount
Bank
Branch
myImage