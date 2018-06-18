from django.views import generic
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView

import os

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage

from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from .models import *
from .forms import *
from django.forms import formset_factory


import csv

# Create your views here.

def register(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
			return redirect('login')

	else:
		f = CustomUserCreationForm()

	return render(request, 'registration/login.html')


def done(request):
	template_name = 'done.html'
	context = {

	"title": "FORM"

	}
	email = EmailMessage(
					'Career Application at BMSIT ',
					'Hi ' + request.user.first_name + ' ,\nWe have received your application for the position of ' + request.user.position + '.',
					[request.user.email] ,
					)
	email.send()
	return render(request, template_name, context)

def logout(request):
	template_name = 'registration/logout.html'
	return render(request, template_name)


class DisplayView(ListView):
	template_name = 'display.html'
	model = User
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context	


def upload_file(request):
	if request.method == 'POST':
		form = FacultyForm(request.POST, request.FILES)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = FacultyForm()

	return render(request, 'index.html', {'form': form})



class PositionView(CreateView):
	User = get_user_model()
	template_name = 'apply.html'
	model = User

	success_url = reverse_lazy("personal")


	error_url = reverse_lazy('personal')
	form_class = ApplyForm

	def get_context_data(self, *args, **kwargs):
		context = super(PositionView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		User = self.request.user
		create.save()
		return HttpResponseRedirect('/personal/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/apply/')

class PersonalView(UpdateView):
	User = get_user_model()
	template_name = 'index.html'
	model = User
	fields = ['place','image','category','nationality','first_name','email' ,'phone' ,	'position' ,'department' ,'fathers_name' ,'address' ,'permanent_address',
	'date_of_birth','age','religion','reservation' ,'family_members' ,
	'kannada_speak','kannada_read' ,'kannada_write' ,
	'english_speak' ,'english_read' ,'english_write',
	'hindi_speak' ,'hindi_read' ,'hindi_write']
	template_name_suffix = 'faculty_update_form'

	def get_object(self):
		print(self.request.user)
		return self.User.objects.get(pk=self.request.user.pk)

	def form_valid(self, form):
		create = form.save()
		return HttpResponseRedirect('/educational/')


class EducationalView(CreateView):
	template_name = 'educational.html'
	model = Course

	success_url = reverse_lazy("industrial")
	error_url = reverse_lazy('educational')
	form_class = EducationalForm


	def get_context_data(self, *args, **kwargs):
		formset = EducationalFormSet(queryset=Course.objects.none())
		context = super(EducationalView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = EducationalFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.Applicant = self.request.user
			create.save()
		formset_valid = formset.is_valid()
		
		return HttpResponseRedirect('/industrial/')

class IndustrialView(CreateView):
	template_name = 'industrial.html'
	model = IndustrialExperience

	success_url = reverse_lazy("teaching")


	error_url = reverse_lazy('industrial')
	form_class = IndustrialForm

	def get_context_data(self, *args, **kwargs):
		formset = IndustrialFormSet(queryset=IndustrialExperience.objects.none())
		context = super(IndustrialView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = IndustrialFormSet(request.POST, request.FILES)
		print(formset)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/teaching/')


class TeachingView(CreateView):
	template_name = 'teaching.html'
	model = TeachingExperience

	success_url = reverse_lazy("research")


	error_url = reverse_lazy('teaching')
	form_class = TeachingForm

	def get_context_data(self, *args, **kwargs):
		formset = TeachingFormSet(queryset=TeachingExperience.objects.none())
		context = super(TeachingView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = TeachingFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/research/')

class ResearchView(CreateView):
	template_name = 'research.html'
	model = Research

	success_url = reverse_lazy("membership")


	error_url = reverse_lazy('research')
	form_class = ResearchForm

	def get_context_data(self, *args, **kwargs):
		context = super(ResearchView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save(commit=False)
		create.faculty = self.request.user
		create.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/membership/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/membership/')

class MembershipView(CreateView):
	template_name = 'membership.html'
	model = Membership

	success_url = reverse_lazy("conference")

	error_url = reverse_lazy('membership')
	form_class = MembershipForm

	def get_context_data(self, *args, **kwargs):
		formset = MembershipFormSet(queryset=Membership.objects.none())
		context = super(MembershipView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = MembershipFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/conference/')

class ConferenceView(CreateView):
	template_name = 'conference.html'
	model = Conference

	success_url = reverse_lazy("reference")


	error_url = reverse_lazy('conference')
	form_class = ConferenceForm

	def get_context_data(self, *args, **kwargs):
		formset = ConferenceFormSet(queryset=Conference.objects.none())
		context = super(ConferenceView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = ConferenceFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/reference/')


class ReferenceView(CreateView):
	template_name = 'reference.html'
	model = Referral

	success_url = reverse_lazy('awards')


	error_url = reverse_lazy('reference')
	form_class = ReferenceForm

	def get_context_data(self, *args, **kwargs):
		formset = ReferenceFormSet(queryset=Referral.objects.none())
		context = super(ReferenceView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = ReferenceFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()


		return HttpResponseRedirect('/awards/')


class AwardsView(CreateView):
	template_name = 'awards.html'
	model = Awards

	success_url = reverse_lazy('achievement')


	error_url = reverse_lazy('awards')
	form_class = AwardForm

	def get_context_data(self, *args, **kwargs):
		context = super(AwardsView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save(commit=False)
		create.faculty = self.request.user
		create.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/achievement/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/achievement/')


class AchievementView(CreateView):
	template_name = 'achievement.html'
	model = SpecialAchievement

	success_url = reverse_lazy("payment")


	error_url = reverse_lazy('achievement')
	form_class = AchievementForm

	def get_context_data(self, *args, **kwargs):
		formset = AchievementFormSet(queryset=SpecialAchievement.objects.none())
		context = super(AchievementView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = AchievementFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.faculty = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/payment/')


class PaymentView(CreateView):
	template_name = 'payment.html'
	model = User

	success_url = reverse_lazy("professional")


	error_url = reverse_lazy('payment')
	form_class = PayementForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(PaymentView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		User = self.request.user
		create.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/documents/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/documents/')

class DocumentsView(CreateView):
	template_name = 'documents.html'
	model = DocumentUpload

	success_url = reverse_lazy("declaration")


	error_url = reverse_lazy('documents')
	form_class = DocumentsForm

	def get_context_data(self, *args, **kwargs):
		formset = DocumentsFormSet(queryset=DocumentUpload.objects.none())
		context = super(DocumentsView, self).get_context_data(*args, **kwargs)
		context['formset'] = formset
		context['user'] = self.request.user.username
		return context
	
	def post(self, request, *args, **kwargs):
		
		formset = DocumentsFormSet(request.POST, request.FILES)
		c = 0
		for forms in formset.forms:
			print(forms.errors)
			print(c)
			c = c +1
			create = forms.save(commit=False)
			create.uploaded_by = self.request.user
			create.save()
		formset_valid = formset.is_valid()

		return HttpResponseRedirect('/declaration/')


class DeclarationView(CreateView):
	template_name = 'declaration.html'
	model = Declaration

	success_url = reverse_lazy("done")

	error_url = reverse_lazy('declaration')
	form_class = DeclarationForm

	def get_context_data(self, *args, **kwargs):
		context = super(DeclarationView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save(commit=False)
		create.faculty = self.request.user
		create.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/done')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/done')

def printView(request):
	template_name='print.html'
	User = get_user_model()
	faculty = User.objects.get(username=request.user.username)
	courses = Course.objects.filter(Applicant=request.user.pk)
	documents = DocumentUpload.objects.filter(uploaded_by=request.user.pk)
	referrals = Referral.objects.filter(faculty=request.user.pk)
	awards = Awards.objects.filter(faculty=request.user.pk)
	industrial = IndustrialExperience.objects.filter(faculty=request.user.pk)
	teaching = TeachingExperience.objects.filter(faculty=request.user.pk)
	membership = Membership.objects.filter(faculty=request.user.pk)
	conference = Conference.objects.filter(faculty=request.user.pk)
	research = Research.objects.filter(faculty=request.user.pk)
	special = SpecialAchievement.objects.filter(faculty=request.user.pk)
	declaration = Declaration.objects.filter(faculty=request.user.pk)
	achievement = SpecialAchievement.objects.filter(faculty=request.user.pk)
	context = {
	"faculty" : faculty,
	"courses" : courses,
	"achievements" : achievement,
	"documents" : documents,
	"referrals" : referrals,
	"awards" : awards,
	"industrial" : industrial,
	"teaching" : teaching,
	"membership" : membership,
	"conference" : conference,
	"research" : research,
	"special" : special,
	"declaration" : declaration,
	}
	print(str(faculty.image.url))
	return render(request, template_name, context)

def admin_print_view(request, email):
	template_name='print.html'
	User = get_user_model()
	current_user = User.objects.get(email=email)
	faculty = User.objects.get(username=current_user.username)
	courses = Course.objects.filter(Applicant=current_user.pk)
	documents = DocumentUpload.objects.filter(uploaded_by=current_user.pk)
	referrals = Referral.objects.filter(faculty=current_user.pk)
	awards = Awards.objects.filter(faculty=current_user.pk)
	industrial = IndustrialExperience.objects.filter(faculty=current_user.pk)
	teaching = TeachingExperience.objects.filter(faculty=current_user.pk)
	membership = Membership.objects.filter(faculty=current_user.pk)
	conference = Conference.objects.filter(faculty=current_user.pk)
	research = Research.objects.filter(faculty=current_user.pk)
	special = SpecialAchievement.objects.filter(faculty=current_user.pk)
	declaration = Declaration.objects.filter(faculty=current_user.pk)
	achievement = SpecialAchievement.objects.filter(faculty=current_user.pk)
	context = {
	"faculty" : faculty,
	"courses" : courses,
	"achievements" : achievement,
	"documents" : documents,
	"referrals" : referrals,
	"awards" : awards,
	"industrial" : industrial,
	"teaching" : teaching,
	"membership" : membership,
	"conference" : conference,
	"research" : research,
	"special" : special,
	"declaration" : declaration,
	}
	print(str(faculty.image.url))
	return render(request, template_name, context)

def export_view(request, file):
	'''
	Downloads the list of remaing students, department wise in a CSV file
	'''
	User = get_user_model()
	faculty_list = User.objects.filter().order_by('email')
	courses = Course.objects.filter()
	referrals = Referral.objects.filter()
	awards = Awards.objects.filter()
	industrial = IndustrialExperience.objects.filter()
	teaching = TeachingExperience.objects.filter()
	membership = Membership.objects.filter()
	conference = Conference.objects.filter()
	research = Research.objects.filter()
	special = SpecialAchievement.objects.filter()

	response = HttpResponse(content_type='text/csv')
	if file == '1':
		response['Content-Disposition'] = 'attachment; filename=user-list.csv'
		writer = csv.writer(response)
		writer.writerow(['username', 'first name', 'email', 'phone', 'fathers name', 'address', 'permanent_address',
			'date of birth', 'age', 'position', 'department', 'place of birth', 'religion', 'reservation', 'category', 'nationality', 'family members', 'kannada speak', 'kannada read', 'kannada write'
			'english speak', 'english read', 'english write', 'hindi speak', 'hindi read', 'hindi write', 'grade', 'no member', 'year of selection', 'neft', 'uti', 'Payment Date', 'Amount',
			'Bank', 'Branch', 'IFSC'])
		for faculty in faculty_list:
			writer.writerow([faculty.username, faculty.first_name, faculty.email, faculty.phone, 
				faculty.fathers_name, faculty.address, faculty.permanent_address, faculty.date_of_birth,
				faculty.age, faculty.position, faculty.department, faculty.place, faculty.religion,
				faculty.reservation, faculty.category, faculty.nationality, faculty.family_members,
				faculty.kannada_speak, faculty.kannada_read, faculty.kannada_write, faculty.english_speak,
				faculty.english_read, faculty.english_write, faculty.hindi_speak, faculty.hindi_read, faculty.hindi_write,
				faculty.grade, faculty.no_member, faculty.year_selection, faculty.neft, faculty.uti, faculty.Date, faculty.Amount, faculty.Bank, faculty.Branch, faculty.ifsc])
		writer.writerow(['Total Applied',(faculty_list.count() - 1)])
	if file == '2':
		response['Content-Disposition'] = 'attachment; filename=course_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone','degree name', 'Specialisation', 'Institution Name', 'Passing Year', 'Percent or grade', 'maximum_marks or grade'])
		for course in courses:
			writer.writerow([course.Applicant.first_name, course.Applicant.email, course.Applicant.phone, 
				course.Degree.name, course.Specialisation, course.Institution_Name, course.Passing_Year, course.Percent_or_grade, course.maximum_marks_or_grade])
	if file == '3':
		response['Content-Disposition'] = 'attachment; filename=referral_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'referral name', 'position', 'designation', 'affiliation', 'contact no', 'email', 'address'])
		for referral in referrals:
			writer.writerow([referral.faculty.first_name, referral.faculty.email, referral.faculty.phone, 
				referral.name, referral.position, referral.designation, referral.affiliation, referral.contact_no, referral.email, referral.address])
	if file == '4':
		response['Content-Disposition'] = 'attachment; filename=award_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'Spec awards particulars', 'state', 'national', 'international'])
		for award in awards:
			writer.writerow([award.faculty.first_name, award.faculty.email, award.faculty.phone, 
				award.Spec_awards_particulars, award.state, award.national, award.international])
	if file == '5':
		response['Content-Disposition'] = 'attachment; filename=industrial-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'organisation', 'position held', 'from date', 'to date', 'experience years'])
		for ind in industrial:
			writer.writerow([ind.faculty.first_name, ind.faculty.email, ind.faculty.phone, 
				ind.organisation, ind.position_held, ind.from_date, ind.to_date, ind.experience_years])
	if file == '6':
		response['Content-Disposition'] = 'attachment; filename=teaching-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'university name', 'designation', 'from date', 'to date', 'total duration'])
		for t in teaching:
			writer.writerow([t.faculty.first_name, t.faculty.email, t.faculty.phone, 
				t.university_name, t.designation, t.from_date, t.to_date, t.total_duration])
	if file == '7':
		response['Content-Disposition'] = 'attachment; filename=membership-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'type of member', 'professional body', 'membership no', 'annual'])
		for t in membership:
			writer.writerow([t.faculty.first_name, t.faculty.email, t.faculty.phone, 
				t.type_of_member, t.professional_body, t.membership_no, t.annual])
	if file == '8':
		response['Content-Disposition'] = 'attachment; filename=conference-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'conf conducted org', 'university', 'from date', 'to date', 'total duration'])
		for t in conference:
			writer.writerow([t.faculty.first_name, t.faculty.email, t.faculty.phone, 
				t.conf_conducted_org, t.university, t.from_date, t.to_date, t.total_duration])
	if file == '9':
		response['Content-Disposition'] = 'attachment; filename=research-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'total experience', 'university', 'area research', 'from date', 'to date', 'total duration'
			'total international conf', 'title paper', 'International', 'year month pub'])
		for t in research:
			writer.writerow([t.faculty.first_name, t.faculty.email, t.faculty.phone, 
				t.total_experience, t.university_name, t.area_reasearch, t.from_date, t.to_date, t.total_duration, t.total_internationalConf,
				t.title_paper, t.conf_International, t.year_month_pub])
	if file == '10':
		response['Content-Disposition'] = 'attachment; filename=special-experience-list_list.csv'
		writer = csv.writer(response)
		writer.writerow(['first name', 'email', 'phone', 'community service', 'industry related', 'university assignment', 'administration'])
		for t in special:
			writer.writerow([t.faculty.first_name, t.faculty.email, t.faculty.phone, 
				t.community_service, t.industry_related, t.university_assignment, t.administration])

	return response


def download_select_view(request):
	template_name = 'download-select.html'
	context = {
		"title": "Download"
	}
	return render(request, template_name, context)

