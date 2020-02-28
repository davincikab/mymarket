from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic import TemplateView
from django.views import View

from .models import User, Profile
from .forms import UserCreateForm


# User create View

class UserCreateView(CreateView):
	model = User
	template_name = "user/register.html"
	success_url = "/"
	form_class = UserCreateForm

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self,form):
		user = form.save(commit=False)
		user.save()
		return HttpResponseRedirect('/')

	def form_invalid(self,form):
		print("Invalid Data")
		return HttpResponseRedirect('/user/register/')

class UserProfile(TemplateView):
	template_name = "user/profile.html"
	# http_method_names = 
	# response_class

	# def get(self):
	# 	pass

	def get_context_data(self, *args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = User.objects.get(username = self.request.user.username)
		return context

	# def render_to_response(self):
	# 	pass

class MyDashBoard(TemplateView):
	template_name = 'user/dashboard.html'
	
	def get_context_data(self, *args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = User.objects.get(username = self.request.user.username)
		return context

