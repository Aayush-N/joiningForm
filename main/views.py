from django.views import generic
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView

import os

from django.shortcuts import render
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
			return redirect('register')

	else:
		f = CustomUserCreationForm()

	return render(request, 'signup.html', {'form': f})


def done(request):
	template_name = 'done.html'
	context = {

	"title": "FORM"

	}
	return render(request, template_name, context)



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




class LoginView(TemplateView):
	template_name = "login.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

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
		return HttpResponseRedirect('/personal/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/apply/')

class PersonalView(UpdateView):
	User = get_user_model()
	template_name = 'index.html'
	model = User
	fields = ['first_name','email' ,'phone' ,	'position' ,'department' ,'fathers_name' ,'address' ,'permanent_address',
	'date_of_birth','age','religion','reservation' ,'family_members' ,
	'kannada_speak','kannada_read' ,'kannada_write' ,
	'english_speak' ,'english_read' ,'english_write',
	'hindi_speak' ,'hindi_read' ,'hindi_write']
	template_name_suffix = 'faculty_update_form'

	def get_object(self):
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
		EducationFormSet = formset_factory(EducationalForm, extra=5)
		context = super(EducationalView, self).get_context_data(*args, **kwargs)
		context['user'] = self.request.user.username
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/industrial/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/industrial/')

class IndustrialView(CreateView):
	template_name = 'industrial.html'
	model = IndustrialExperience

	success_url = reverse_lazy("teaching")


	error_url = reverse_lazy('industrial')
	form_class = IndustrialForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(IndustrialView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/teaching/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/teaching/')


class TeachingView(CreateView):
	template_name = 'teaching.html'
	model = TeachingExperience

	success_url = reverse_lazy("research")


	error_url = reverse_lazy('teaching')
	form_class = TeachingForm

	def get_context_data(self, *args, **kwargs):
		context = super(TeachingView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/research/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/research/')

class ResearchView(CreateView):
	template_name = 'research.html'
	model = Research

	success_url = reverse_lazy("conference")


	error_url = reverse_lazy('research')
	form_class = ResearchForm

	def get_context_data(self, *args, **kwargs):
		context = super(ResearchView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/conference/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/conference/')

class ConferenceView(CreateView):
	template_name = 'conference.html'
	model = TeachingExperience

	success_url = reverse_lazy("payment")


	error_url = reverse_lazy('conference')
	form_class = TeachingForm

	def get_context_data(self, *args, **kwargs):
		context = super(ConferenceView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		print(self.request.FILES)
		return HttpResponseRedirect('/payment/')
	
	def form_invalid(self,form):
		print(form.errors)

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

		print(self.request.FILES)
		return HttpResponseRedirect('/documents/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/documents/')

class DocumentsView(CreateView):
	template_name = 'documents.html'
	model = DocumentUpload

	success_url = reverse_lazy("done")


	error_url = reverse_lazy('documents')
	form_class = DocumentsForm

	def get_context_data(self, *args, **kwargs):
		DocumentFormSet = formset_factory(DocumentUpload, extra=10)
		context = super(DocumentsView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/done')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/done')








