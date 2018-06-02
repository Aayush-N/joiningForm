from django import forms

from .models import *

class ApplyForm(forms.ModelForm):
	class Meta:
		model = ApplyPositions
		fields = ('__all__')

class FacultyForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')

class PersonalForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')

class EducationalForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')

class ProfessionalForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')

class PayementForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')

class DocumentsForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ('__all__')