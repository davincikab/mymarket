from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic import TemplateView
from django.views import View
from django.db.models import Q, Sum

from .models import User, Profile, Certification, Academic
from market.models import Messages, Orders
from .forms import UserCreateForm, AcademicCreateForm, CertificationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

class UserProfile(LoginRequiredMixin,TemplateView):
	template_name = "user/profile.html"

	def get_context_data(self, *args,**kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(username=self.request.user.username)
		context['user'] = User.objects.get(username = self.request.user.username)
		context['orders_sold'] = Orders.objects.filter(awarded_to=self.request.user).count() 
		context['orders_bought'] = Orders.objects.filter(project__created_by =self.request.user).count()
		context['Amount Spent'] = Orders.objects.filter(project__created_by =self.request.user).annotate(total=Sum('cost')).values('total')
		context['earning'] = Orders.objects.filter(awarded_to=self.request.user).annotate(total=Sum('cost')).values('total')
		
		if Certification.objects.filter(user=user): 
			initial_cert_data = Certification.objects.get(user=user) 
		else:
			initial_cert_data = {'user':user}

		context['form_certificate'] = CertificationCreateForm(initial = initial_cert_data)

		if Academic.objects.filter(user=user):
			initial_academic_data = Academic.objects.filter(user = user)
		else:
			initial_academic_data = {'user': user}
			
		context['form_academic'] = AcademicCreateForm(initial=initial_academic_data)
		return context

	# def render_to_response(self):
	# 	pass


class MyDashBoard(LoginRequiredMixin, TemplateView):
	template_name = 'user/dashboard.html'
	
	def get_context_data(self, *args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = User.objects.get(username = self.request.user.username)
		context['messages'] = Messages.objects.filter(reciever=self.request.user)
		context['recieved'] = Messages.objects.filter(reciever = self.request.user)
		context['conversation'] = Messages.objects.filter(Q(reciever=self.request.user) | Q(sender=self.request.user)).order_by('created_on')

		print(context['conversation'])
		return context


class MyMessages(LoginRequiredMixin, View):
	def get(self, request,*args,**kwargs):
		# Filter depending on the user
		context['conversation'] = Messages.objects.filter(
			Q(reciever=self.request.user) | Q(sender=self.request.user)).order_by('created_on')
		messages = Messages.objects.filter(sender=self.request.user)
		return HttpResponse("Messages")

@login_required(login_url='/user/login/')
def get_user_profile(request, userid):
	user = get_object_or_404(User,pk = userid)
	context = {}
	context['user'] = user
	context['orders_sold'] = Orders.objects.filter(awarded_to=user).count()
	context['orders_sold_complete'] = Orders.objects.filter(awarded_to=user).filter(isdone=True).count()
	context['orders_bought'] = Orders.objects.filter(project__created_by=user).count()
	context['Amount Spent'] = Orders.objects.filter(project__created_by=user).annotate(total=Sum('cost')).values('total')
	context['earning'] = Orders.objects.filter(awarded_to=user).annotate(total=Sum('cost')).values('total')

	return render(request, 'user/profile.html',context)
