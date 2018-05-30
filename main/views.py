from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 

from .models import *
from .forms import *

# Create your views here.

class IndexView(CreateView):
	template_name = 'index.html'
	model = Faculty
	#success_url = reverse("index")
	error_url = reverse_lazy('index')
	form_class = FacultyForm

	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = form.save()
		return HttpResponseRedirect('/done')

def done(request):
	template_name = 'done.html'
	context = {
	"title": "JobsRubix"
	}
	return render(request, template_name, context)

class DisplayView(ListView):
	template_name = 'display.html'
	model = Faculty
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