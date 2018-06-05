from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Positions(models.Model):
	name = models.CharField(max_length=40)
	def __str__(self):
		return self.name


class ApplyPositions(models.Model):
	name = models.ForeignKey("Positions", on_delete=models.CASCADE, null=False)
	def __str__(self):
		return self.name

class Proficiency(models.Model):
	proficiency = models.CharField("proficiency", max_length=50, null=False, blank=False)
	def __str__(self):
		return self.proficiency


class User(AbstractUser):
	image = models.FileField(upload_to='uploads/', blank=True,null=True)
	email = models.EmailField('email address', unique=True)
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	position = models.CharField(max_length=20, null=True, blank=True)
	department = models.CharField(max_length=50, null=True, blank=True)
	fathers_name = models.CharField(max_length=50, null=True, blank=True)
	address = models.CharField(max_length=50, null=True, blank=True)
	permanent_address = models.CharField(max_length=50, null=True, blank=True)
	date_of_birth = models.DateField(max_length=8, null=True, blank=True)
	age = models.IntegerField(null=True, blank=True) 
	place = models.CharField(max_length=50, null=True, blank=True)
	religion = models.CharField(max_length=50, null=True, blank=True)
	reservation = models.CharField(max_length=50, null=True, blank=True)
	category = models.CharField(max_length=50, null=True, blank=True)
	nationality = models.CharField(max_length=50, null=True, blank=True)
	family_members = models.IntegerField(default=0)
	kannada_speak = models.BooleanField(default=False)
	kannada_read = models.BooleanField(default=False)
	kannada_write = models.BooleanField(default=False)
	english_speak = models.BooleanField(default=False)
	english_read = models.BooleanField(default=False)
	english_write = models.BooleanField(default=False)
	hindi_speak = models.BooleanField(default=False)
	hindi_read = models.BooleanField(default=False)
	hindi_write = models.BooleanField(default=False)
	grade = models.CharField("grade", max_length=50, null=True, blank=True)
	no_member = models.CharField("members", max_length=50, null=True, blank=True)
	year_selection = models.CharField("year selection", max_length=50, null=True, blank=True)
	#BankDetails
	neft = models.CharField("NEFT", max_length=50, null=True, blank=True)
	uti = models.CharField("UTR", max_length=35, null=True, blank=True)
	Date = models.CharField("Date", max_length=35, null=True, blank=True)
	Amount = models.CharField("Amount", max_length=35, null=True, blank=True, default='500')
	Bank = models.CharField("Bank", max_length=35, null=True, blank=True)
	Branch = models.CharField("Branch", max_length=35, null=True, blank=True)
	ifsc = models.CharField("IFSC", max_length=10, null=True, blank=True)

	#FilesToBeUploaded
	# Sslc = models.FileField(upload_to='uploads/')
	# bachelors_certificate = models.FileField(upload_to='uploads/')
	# bachelors_marks_card = models.FileField(upload_to='uploads/')
	# masters_certificate = models.FileField(upload_to='uploads/')
	# masters_marks_card = models.FileField(upload_to='uploads/')
	# phd_certificate = models.FileField(upload_to='uploads/')
	# other_certificate = models.FileField(upload_to='uploads/')
	# research_experience_certificate = models.FileField(upload_to='uploads/')
	# teaching_experience_certificate = models.FileField(upload_to='uploads/')
	# industrial_experience_certificate = models.FileField(upload_to='uploads/')
	# research_publication_certificate = models.FileField(upload_to='uploads/')
	# professional_membership_certificate = models.FileField(upload_to='uploads/')
	# aadhar_card = models.FileField(upload_to='uploads/')
	# pan_card = models.FileField(upload_to='uploads/')
	# reference_letter1 = models.FileField(upload_to='uploads/')
	# reference_letter2 = models.FileField(upload_to='uploads/')
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def is_admin(self):
		return self.groups.filter(name='Admin').exists()

	def __str__(self):
		return self.username

class Degree(models.Model):
	"""
	Description: The Degree
	"""	
	name = models.CharField(max_length=50, null=False, blank=False)
	def __str__(self):
		return self.name

class Course(models.Model):
	Applicant = models.ForeignKey("User", on_delete=models.CASCADE)
	Degree = models.ForeignKey("Degree", on_delete=models.CASCADE)
	Specialisation = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year = models.CharField(max_length=50, null=False, blank=False)
	Percent_or_grade = models.CharField(max_length=50, null=False, blank=False)
	maximum_marks_or_grade = models.CharField(max_length=50, null=False, blank=False)
	file_upload = models.FileField(upload_to='uploads/')

	def __str__(self):
		return self.Applicant.username

class DocumentType(models.Model):
	type_of_document = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.type_of_document


class DocumentUpload(models.Model):
	"""
	Description: Model Description
	"""
	uploaded_by = models.ForeignKey("User", on_delete=models.CASCADE)
	type_of_document = models.ForeignKey("DocumentType", on_delete=models.CASCADE)
	file =  models.FileField(upload_to='uploads/')

	def __str__(self):
		return self.uploaded_by.first_name


class Referral(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	name = models.CharField("name", max_length=50, null=False, blank=False)
	position = models.CharField("position", max_length=50, null=False, blank=False)
	designation = models.CharField("designation", max_length=50, null=False, blank=False)
	affiliation = models.CharField("affiliation", max_length=50, null=False, blank=False)
	contact_no = models.CharField("contact no", max_length=50, null=False, blank=False)
	email = models.CharField("email", max_length=50, null=False, blank=False)
	address = models.CharField("address", max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name


class Awards(models.Model):
	"""
	Description: Model Description
	"""
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	Spec_awards_particulars = models.CharField("Particulars", max_length=50, null=False, blank=False)
	state = models.CharField("State", max_length=50, null=False, blank=False)
	national = models.CharField("National", max_length=50, null=False, blank=False)
	international = models.CharField("International", max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name


class IndustrialExperience(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	organisation = models.CharField("organisation", max_length=50, null=False, blank=False)
	position_held = models.CharField("position held", max_length=50, null=False, blank=False)
	from_date = models.CharField("from date", max_length=50, null=False, blank=False)
	to_date = models.CharField("to date", max_length=50, null=False, blank=False)
	experience_years = models.CharField("experience years", max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name


class TeachingExperience(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	university_name = models.CharField(max_length=50, null=True, blank=False)
	designation = models.CharField(max_length=50, null=True, blank=False)
	from_date = models.CharField("from", max_length=50, null=False, blank=False)
	to_date = models.CharField("to", max_length=50, null=False, blank=False)
	total_duration = models.CharField("total duration", max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name

class Membership(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	type_of_member = models.CharField(max_length=50,null=True, blank=False)
	professional_body = models.CharField(max_length=50, null=True, blank=False)
	membership_no = models.CharField(max_length=50, null=True, blank=False)
	annual = models.CharField(max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name


class Conference(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	conf_conducted_org = models.CharField("organisation", max_length=50, null=False, blank=False)
	total_experience = models.CharField("experience", max_length=50, null=False, blank=False)
	university = models.CharField("university", max_length=50, null=False, blank=False)
	designation = models.CharField("designationsi", max_length=50, null=False, blank=False)
	from_date = models.CharField("from", max_length=50, null=True, blank=False)
	to_date = models.CharField("to", max_length=50, null=True, blank=False)
	total_duration = models.CharField("total duration", max_length=50, null=True, blank=False)
	def __str__(self):
		return self.faculty.first_name

class Research(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	total_experience = models.CharField(max_length=50, null=False, blank=False)
	university_name = models.CharField(max_length=50, null=False, blank=False)
	area_reasearch = models.CharField(max_length=50, null=False, blank=False)
	from_date = models.CharField(max_length=50, null=False, blank=False)
	to_date = models.CharField(max_length=50, null=False, blank=False)
	total_duration = models.CharField(max_length=50, null=False, blank=False)
	total_internationalConf = models.CharField(max_length=50, null=False, blank=False)
	title_paper = models.CharField(max_length=50, null=False, blank=False)
	conf_International = models.CharField(max_length=50, null=False, blank=False)
	year_month_pub = models.CharField(max_length=50, null=False, blank=False)
	def __str__(self):
		return self.faculty.first_name

class SpecialAchievement(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	community_service = models.CharField("community services", max_length=250, null=True, blank=True)
	industry_related = models.CharField("industry related", max_length=50, null=True, blank=True)
	university_assignment = models.CharField("university assignment", max_length=50, null=True, blank=True)
	administration = models.CharField("administration", max_length=50, null=True, blank=True)

class Declaration(models.Model):
	faculty = models.ForeignKey("User", on_delete=models.CASCADE)
	signature = models.FileField(upload_to='uploads/')