from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Projects, Orders, Messages
from .forms import OrdersCreateForm, MessagesCreateForm, ProjectsCreateForm

# Create your views here.
def home(request):
	return render(request,'index.html')

class CommunityView(TemplateView):
	template_name = 'index.html'

	def get(self):
		self.object = User.objects.all()

	def get_context_data(self,*args,**kwargs):
		context = self.object
		return context 

class ProjectsListView(ListView):
	model = Projects
	template_name = 'index.html'
	contex_object_name = "projects",
	paginate_by = 25

	def get_queryset(self):
		return super().get_queryset()

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectDetailView(DetailView):
	model = Projects
	template_name = 'index.html'
	contex_object_name = 'project'

	def get_queryset(self):
		return super().get_queryset()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectUpdateView(UpdateView):
	model = Projects
	template_name = 'project_create.html'
	form_class = ProjectsCreateForm
	extra_context = "Update Project"

class ProjectCreateForm(CreateView):
	model = Projects
	template_name = 'project_create.html'
	form_class = ProjectCreateForm
	extra_context = "Create Project"

# ========================= END OF PROJECTS ===============
class OrdersListView(ListView):
	models = Orders
	template_name = 'orders.html'

c