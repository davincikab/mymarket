from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Projects, Orders, Messages
from .forms import OrdersCreateForm, MessagesCreateForm, ProjectsCreateForm

from user.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		messages = Messages.objects.filter(sender=request.user)
	else:
		messages = {}
	return render(request,'home.html',{'messages':messages})

class CommunityView(LoginRequiredMixin,TemplateView):
	template_name = 'community.html'
	paginate_by = 25

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['users'] = User.objects.all()
		return context 

class ProjectsListView(LoginRequiredMixin,ListView):
	model = Projects
	template_name = 'projects.html'
	context_object_name = "projects"
	paginate_by = 25
	ordering = '-create_at'

	def get_queryset(self):
		return Projects.objects.filter(awarded=False)

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

class ProjectDetailView(LoginRequiredMixin,DetailView):
	model = Projects
	template_name = 'project_detail.html'
	context_object_name = 'project'

	def get_queryset(self):
		return super().get_queryset()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
	model = Projects
	template_name = 'project_create.html'
	form_class = ProjectsCreateForm
	extra_context = {'name':"Update Project"}

class ProjectCreateView(LoginRequiredMixin,CreateView):
	model = Projects
	template_name = 'project_create.html'
	form_class = ProjectsCreateForm
	extra_context = {'name':"Create Project"}

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
	model = Projects
	template_name = 'project_delete.html'
	extra_context = {'name': 'Delete Project'}
	success_url = reverse_lazy('project-list')

# ========================= END OF PROJECTS ===============


class OrderListView(LoginRequiredMixin, ListView):
	model = Orders
	template_name = 'orders.html'
	context_object_name = "orders"

	def get_queryset(self):
		return super().get_queryset().filter(awarded_to=self.request.user)
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
	
class OrderDetailView(LoginRequiredMixin, DetailView):
	model = Orders
	template_name = 'order_detail.html'
	context_object_name = "order"

	def get_queryset(self):
		return super().get_queryset()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		order = Orders.objects.get(orderid = self.kwargs['pk'])
		host = self.request.get_host()

		paypal_dict = {
        'business': settings.PERSONAL_RECIEVER_EMAIL,
        'amount': order.cost,
        'item_name': f'Order {order.orderid}',
        'invoice': order.orderid,
		'currency_code':'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("payment-done")}',
        'cancel_return': f'http://{host}{reverse("payment-cancelled")}',
        'custom': 'premium_plan'
		}

		context['form'] = PayPalPaymentsForm(initial=paypal_dict)

		return context
	

class OrderCreateView(LoginRequiredMixin, CreateView):
	model = Orders
	form_class = OrdersCreateForm
	template_name = 'orders_create.html'
	extra_context = {'name':'Create Order'}


class OrderUpateView(LoginRequiredMixin, UpdateView):
	model = Orders
	form_class = OrdersCreateForm
	template_name = 'orders_create.html'
	extra_context = {'name':'Update Order'}


class OrderDeleteView(LoginRequiredMixin, DeleteView):
	model = Orders
	template_name = 'orders.html'
	# success_url = reverse('home')

# ============= END OF ORDERS ===================


def make_payment(request):
    return render(request, 'payment/payment.html')

@csrf_exempt
def payment_done(request):
    return render(request,'payment/payment_done.html')

@csrf_exempt
def payment_cancelled(request):
	return render(request,'payment/payment_cancelled.html')





