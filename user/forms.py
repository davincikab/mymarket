from .models import User, Profile, Academic,Certification
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields+('middle_name',)
		# widgets

class CertificationCreateForm(forms.ModelForm):
	class Meta:
		model = Certification
		fields = '__all__'

class AcademicCreateForm(forms.ModelForm):
	class Meta:
		model = Academic
		fields = '__all__'