from django import forms
from .models import Projects, Orders, Messages

class ProjectsCreateForm(forms.ModelForm):
	# Initialize the values, preprocessing
	class Meta:
		models = Projects
		fields = "__all__"

class MessagesCreateForm(forms.ModelForm):
	class Meta:
		models = Messages
		fields = "__all__"


class OrdersCreateForm(forms.ModelForm):
	class Meta:
		models = Orders
		fields = "__all__"