from django import forms

from .models import *

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory


class CustomUserCreationForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	email = forms.EmailField(label='Enter email')
	password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		User = get_user_model()
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise  ValidationError("Username already exists")
		return username

	def clean_email(self):
		User = get_user_model()
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise  ValidationError("Email already exists")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Password don't match")

		return password2

	def save(self, commit=True):
		User = get_user_model()
		user = User.objects.create_user(
			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password1']
		)
		return user


class ApplyForm(forms.ModelForm):
	class Meta:
		model = ApplyPositions
		fields = ('__all__')


class PersonalForm(forms.ModelForm):
	class Meta:
		User = get_user_model()
		model = User
		fields = ('__all__')

class EducationalForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('__all__')
		exclude = ('Applicant',)


EducationalFormSet = modelformset_factory(Course, form=EducationalForm, extra=15)


class IndustrialForm(forms.ModelForm):
	class Meta:
		model = IndustrialExperience
		fields = ('__all__')
		exclude = ('faculty',)

class TeachingForm(forms.ModelForm):
	class Meta:
		model = TeachingExperience
		fields = ('__all__')
		exclude = ('faculty',)

class ResearchForm(forms.ModelForm):
	class Meta:
		model = Research
		fields = ('__all__')
		exclude = ('faculty',)

class MembershipForm(forms.ModelForm):
	class Meta:
		model = Membership
		fields = ('__all__')
		exclude = ('faculty',)

class ConferenceForm(forms.ModelForm):
	class Meta:
		model = Conference
		fields = ('__all__')
		exclude = ('faculty',)

class AwardForm(forms.ModelForm):
	class Meta:
		model = Awards
		fields = ('__all__')
		exclude = ('faculty',)

class ReferenceForm(forms.ModelForm):
	class Meta:
		model = Referral
		fields = ('__all__')
		exclude = ('faculty',)

class AchievementForm(forms.ModelForm):
	class Meta:
		model = SpecialAchievement
		fields = ('__all__')
		exclude = ('faculty',)

class PayementForm(forms.ModelForm):
	class Meta:
		User = get_user_model()
		model = User
		fields = ('__all__')

class DocumentsForm(forms.ModelForm):
	class Meta:
		model = DocumentUpload
		fields = ('__all__')
		exclude = ('uploaded_by',)

class DeclarationForm(forms.ModelForm):
	class Meta:
		model = Declaration
		fields = ('__all__')
		exclude = ('faculty',)