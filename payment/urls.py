from django.urls import path
from .views import make_payment, update_payment
urlpatterns = [
    path('pay/', make_payment, name='payment'),
    path('update_payment/', update_payment, name='update-payment')
]