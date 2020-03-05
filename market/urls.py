from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import home, ProjectsListView, OrderListView, CommunityView
from .views import ProjectDetailView, ProjectUpdateView,ProjectCreateView, ProjectDeleteView
from .views import OrderCreateView, OrderDeleteView, OrderDetailView, OrderListView

from .views import payment_cancelled, payment_done, make_payment

urlpatterns = [
	path('', home, name="home"),
	path('projects/', ProjectsListView.as_view(), name="project-list"),
	path('projects/detail/<slug:pk>/', ProjectDetailView.as_view(), name="project-detail"),
	path('projects/update/<slug:pk>/',ProjectUpdateView.as_view(), name="project-update"),
	path('projects/create/',ProjectCreateView.as_view(), name="project-create"),
	path('projects/delete/<slug:pk>/', ProjectDeleteView.as_view(), name="project-delete"),

	path('orders/',OrderListView.as_view(), name="order-list"),
	path('orders/detail/<slug:pk>/', OrderDetailView.as_view(), name="order-details"),
	path('orders/create/', OrderCreateView.as_view(), name="order-create"),
	path('orders/delete/<slug:pk>/', OrderDeleteView.as_view(), name="order-delete"),

	path('community/', CommunityView.as_view(), name='community'),

    path('payment/', make_payment, name='paypal-ipn'),
    path('payment-done/', payment_done, name='payment-done'),
    path('payment-cancelled/', payment_cancelled, name='payment-cancelled')
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
