from django.db import models

# Create your models here.

class Languages(models.Model):
	proficiency = models.CharField("proficiency", max_length=50, null=False, blank=False)

class PHD(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class MTech(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class MphilMca(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class BE(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class Bsc(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class OtherCourse(models.Model):
	Course = models.CharField(max_length=50, null=False, blank=False)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded = models.CharField(max_length=50, null=False, blank=False)

class Research(models.Model):
	total_researchExp = models.CharField(max_length=50, null=False, blank=False)
	Name_university = models.CharField(max_length=50, null=False, blank=False)
	area_reasearch = models.CharField(max_length=50, null=False, blank=False)
	from_date = models.CharField(max_length=50, null=False, blank=False)
	to_date = models.CharField(max_length=50, null=False, blank=False)
	total_duration = models.CharField(max_length=50, null=False, blank=False)
	total_internationalConf = models.CharField(max_length=50, null=False, blank=False)
	title_paper = models.CharField(max_length=50, null=False, blank=False)
	conf_International = models.CharField(max_length=50, null=False, blank=False)
	year_month_pub = models.CharField(max_length=50, null=False, blank=False)

class Conference(models.Model):
	conf_conducted_org = models.CharField("organisation", max_length=50, null=False, blank=False)
	total_experience = models.CharField("experience", max_length=50, null=False, blank=False)
	university = models.CharField("university", max_length=50, null=False, blank=False)
	designation = models.CharField("designationsi", max_length=50, null=False, blank=False)
	from_date = models.CharField("from", max_length=50, null=False, blank=False)
	to_date = models.CharField("to", max_length=50, null=False, blank=False)
	total_duration = models.CharField("total duration", max_length=50, null=False, blank=False)

class Affiliation(models.Model):
	profbody = models.CharField("body", max_length=50, null=False, blank=False)
	grade = models.CharField("grade", max_length=50, null=False, blank=False)
	no_member = models.CharField("members", max_length=50, null=False, blank=False)
	year_selection = models.CharField("year selection", max_length=50, null=False, blank=False)
class IndustrialExperience(models.Model):
	organisation = models.CharField("organisation", max_length=50, null=False, blank=False)
	position_held = models.CharField("position held", max_length=50, null=False, blank=False)
	from_date = models.CharField("from date", max_length=50, null=False, blank=False)
	to_date = models.CharField("to date", max_length=50, null=False, blank=False)
	experience_years = models.CharField("experience years", max_length=50, null=False, blank=False)

class Awards(models.Model):
	Spec_awards_particulars = models.CharField("Particulars", max_length=50, null=False, blank=False)
	state = models.CharField("State", max_length=50, null=False, blank=False)
	national = models.CharField("National", max_length=50, null=False, blank=False)
	international = models.CharField("International", max_length=50, null=False, blank=False)

class Referral(models.Model):
	name = models.CharField("name", max_length=50, null=False, blank=False)
	position = models.CharField("position", max_length=50, null=False, blank=False)
	contact_no = models.CharField("contact no", max_length=50, null=False, blank=False)

class BankDetails(models.Model):
	neft = models.CharField("NEFT", max_length=50, null=False, blank=False)
	uti = models.CharField("UTI", max_length=35, null=False, blank=False)
	Date = models.CharField("Date", max_length=35, null=False, blank=False)
	Amount = models.CharField("Amount", max_length=35, null=False, blank=False)
	Bank = models.CharField("Bank", max_length=35, null=False, blank=False)
	Branch = models.CharField("Branch", max_length=35, null=False, blank=False)




class Faculty(models.Model):
	position = models.CharField(max_length=20)
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
	Kannada = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='kannada')
	English = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='english')
	Hindi = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='hindi')
	PHD = models.ForeignKey("PHD", on_delete=models.CASCADE, null=True)
	MTech = models.ForeignKey("MTech", on_delete=models.CASCADE, null=True)
	MphilMca = models.ForeignKey("MphilMca", on_delete=models.CASCADE, null=True)
	BE = models.ForeignKey("BE", on_delete=models.CASCADE, null=True)
	Bsc = models.ForeignKey("Bsc", on_delete=models.CASCADE, null=True)
	OtherCourse = models.ForeignKey("OtherCourse", on_delete=models.CASCADE, null=True)
	Research = models.ForeignKey("Research", on_delete=models.CASCADE, null=True)
	Conference = models.ForeignKey("Conference", on_delete=models.CASCADE, null=True)
	Affiliation =models.ForeignKey("Affiliation", on_delete=models.CASCADE, null=True)
	IndustrialExperience =models.ForeignKey("IndustrialExperience", on_delete=models.CASCADE, null=True)
	Awards = models.ForeignKey("Awards", on_delete=models.CASCADE, null=True)
	Referral = models.ForeignKey("Referral", on_delete=models.CASCADE, null=True)
	BankDetails = models.ForeignKey("BankDetails", on_delete=models.CASCADE, null=True)