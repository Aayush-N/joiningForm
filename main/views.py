from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView
import os
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 

from .models import *
from .forms import *

import csv

# Create your views here.

class IndexView(CreateView):
	template_name = 'index.html'
	model = Faculty

	success_url = reverse_lazy("index")


	error_url = reverse_lazy('index')
	form_class = FacultyForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(IndexView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/done')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/done')


def done(request):
	template_name = 'done.html'
	context = {

	"title": "FORM"

	}
	return render(request, template_name, context)

class DisplayView(ListView):
	template_name = 'display.html'
	model = Faculty
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
	template_name = 'apply.html'
	model = Faculty

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


class personalView(CreateView):
	template_name = 'index.html'
	model = Faculty

	success_url = reverse_lazy("educational")


	error_url = reverse_lazy('personal')
	form_class = PersonalForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(personalView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print('sfnsjbsjfbsjbfsjbsbsjbsfjfbsfbswbfsjfbsjf')
		return HttpResponseRedirect('/educational/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/educational/')

class educationalView(CreateView):
	template_name = 'educational.html'
	model = Faculty

	success_url = reverse_lazy("professional")


	error_url = reverse_lazy('educational')
	form_class = EducationalForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(educationalView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/professional/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/professional/')

class professionalView(CreateView):
	template_name = 'professional.html'
	model = Faculty

	success_url = reverse_lazy("payment")


	error_url = reverse_lazy('professional')
	form_class = ProfessionalForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(professionalView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/payment/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/payment/')

class paymentView(CreateView):
	template_name = 'payment.html'
	model = Faculty

	success_url = reverse_lazy("professional")


	error_url = reverse_lazy('payment')
	form_class = PayementForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(paymentView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/documents/')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/documents/')

class documentsView(CreateView):
	template_name = 'documents.html'
	model = Faculty

	success_url = reverse_lazy("done")


	error_url = reverse_lazy('documents')
	form_class = DocumentsForm

	def get_context_data(self, *args, **kwargs):

		

		context = super(documentsView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()

		print(self.request.FILES)
		return HttpResponseRedirect('/done')
	
	def form_invalid(self,form):
		print(form.errors)

		return HttpResponseRedirect('/done')








