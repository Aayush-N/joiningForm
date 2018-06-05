from django.views import generic
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView

import os

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

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



def ExportView(request):
	with open(os.path.join("/"), "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
	data = Faculty.objects.all()
	print(data)
	for line in data:
		writer.writerow(line)

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

	context = {
	"faculty" : faculty,
	"courses" : courses,
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

	return render(request, template_name, context)




