from django.db import models

# Create your models here.

class Faculty(models.Model):
	position = models.CharField(max_length=20)
	department = models.CharField(max_length=50)
	name = models.CharField(max_length=50, blank=False, null=False)
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
	proficiency_kannada = models.CharField("proficiency", max_length=50, null=False, blank=False)
	proficiency_english = models.CharField("proficiency", max_length=50, null=False, blank=False)
	proficiency_hindi = models.CharField("proficiency", max_length=50, null=False, blank=False)
	# Kannada = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='kannada')
	# English = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='english')
	# Hindi = models.ForeignKey("Languages", on_delete=models.CASCADE, null=False,related_name='hindi')
	Course_phd = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_phd = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_phd = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_phd = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_phd = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_phd = models.CharField(max_length=50, null=False, blank=False)

	Course_mtech = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_mtech = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_mtech = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_mtech = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_mtech = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_mtech = models.CharField(max_length=50, null=False, blank=False)

	Course_mca = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_mca = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_mca = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_mca = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_mca = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_mca = models.CharField(max_length=50, null=False, blank=False)

	Course_be = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_be = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_be = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_be = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_be = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_be = models.CharField(max_length=50, null=False, blank=False)

	Course_bsc = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_bsc = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_bsc = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_bsc = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_bsc = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_bsc = models.CharField(max_length=50, null=False, blank=False)

	Course_other = models.CharField(max_length=50, null=False, blank=False)
	Specialisation_other = models.CharField(max_length=50, null=False, blank=False)
	Institution_Name_other = models.CharField(max_length=50, null=False, blank=False)
	Passing_Year_other = models.CharField(max_length=50, null=False, blank=False)
	Percent_Marks_other = models.CharField(max_length=50, null=False, blank=False)
	Class_Awarded_other = models.CharField(max_length=50, null=False, blank=False)

	#research
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

	#Conference
	conf_conducted_org = models.CharField("organisation", max_length=50, null=False, blank=False)
	total_experience = models.CharField("experience", max_length=50, null=False, blank=False)
	university = models.CharField("university", max_length=50, null=False, blank=False)
	designation = models.CharField("designationsi", max_length=50, null=False, blank=False)

	from_date_conf = models.CharField("from", max_length=50, null=True, blank=False)
	to_date_conf = models.CharField("to", max_length=50, null=True, blank=False)
	total_duration_conf = models.CharField("total duration", max_length=50, null=True, blank=False)

	#teaching
	university_name = models.CharField(max_length=50, null=True, blank=False)
	designation = models.CharField(max_length=50, null=True, blank=False)
	from_date_teaching = models.CharField(max_length=50, null=True, blank=False)
	to_date_teaching = models.CharField(max_length=50, null=True, blank=False)
	total_duration_teaching = models.CharField(max_length=50, null=True, blank=False)

	from_date = models.CharField("from", max_length=50, null=False, blank=False)
	to_date = models.CharField("to", max_length=50, null=False, blank=False)
	total_duration = models.CharField("total duration", max_length=50, null=False, blank=False)


	#Affiliation
	profbody = models.CharField("body", max_length=50, null=False, blank=False)
	grade = models.CharField("grade", max_length=50, null=False, blank=False)
	no_member = models.CharField("members", max_length=50, null=False, blank=False)
	year_selection = models.CharField("year selection", max_length=50, null=False, blank=False)

	#IndustrialExperience
	organisation = models.CharField("organisation", max_length=50, null=False, blank=False)
	position_held = models.CharField("position held", max_length=50, null=False, blank=False)

	from_date_industrial = models.CharField("from date", max_length=50, null=True, blank=False)
	to_date_industrial = models.CharField("to date", max_length=50, null=True, blank=False)

	from_date = models.CharField("from date", max_length=50, null=False, blank=False)
	to_date = models.CharField("to date", max_length=50, null=False, blank=False)

	experience_years = models.CharField("experience years", max_length=50, null=False, blank=False)

	#Awards
	Spec_awards_particulars = models.CharField("Particulars", max_length=50, null=False, blank=False)
	state = models.CharField("State", max_length=50, null=False, blank=False)
	national = models.CharField("National", max_length=50, null=False, blank=False)
	international = models.CharField("International", max_length=50, null=False, blank=False)

	#Referral
	name = models.CharField("name", max_length=50, null=False, blank=False)
	position = models.CharField("position", max_length=50, null=False, blank=False)
	contact_no = models.CharField("contact no", max_length=50, null=False, blank=False)

	#BankDetails
	neft = models.CharField("NEFT", max_length=50, null=False, blank=False)
	uti = models.CharField("UTI", max_length=35, null=False, blank=False)
	Date = models.CharField("Date", max_length=35, null=False, blank=False)
	Amount = models.CharField("Amount", max_length=35, null=False, blank=False)
	Bank = models.CharField("Bank", max_length=35, null=False, blank=False)
	Branch = models.CharField("Branch", max_length=35, null=False, blank=False)

	#FilesToBeUploaded
	Sslc = models.FileField(upload_to='uploads/')
	bachelors_certificate = models.FileField(upload_to='uploads/')
	bachelors_marks_card = models.FileField(upload_to='uploads/')
	masters_certificate = models.FileField(upload_to='uploads/')
	masters_marks_card = models.FileField(upload_to='uploads/')
	phd_certificate = models.FileField(upload_to='uploads/')
	other_certificate = models.FileField(upload_to='uploads/')
	research_experience_certificate = models.FileField(upload_to='uploads/')
	teaching_experience_certificate = models.FileField(upload_to='uploads/')
	industrial_experience_certificate = models.FileField(upload_to='uploads/')
	research_publication_certificate = models.FileField(upload_to='uploads/')
	professional_membership_certificate = models.FileField(upload_to='uploads/')
	aadhar_card = models.FileField(upload_to='uploads/')
	pan_card = models.FileField(upload_to='uploads/')
	reference_letter1 = models.FileField(upload_to='uploads/')
	reference_letter2 = models.FileField(upload_to='uploads/')
	

	def __str__(self):
		return self.name

