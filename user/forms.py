from .models import User, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields+('middle_name',)
		# widgets