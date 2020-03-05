from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

def make_payment(request):
    # Extract the project and order id
    paypal_dict = {
        'business':'david@gmail.com',
        'amount':'2000',
        'item_name':'project_name',
        'invoice':'order_id',
        'notify_url':reverse('update-payment'),
        'return':reverse('update-payment'),
        'cancel_return':reverse('payment'),
        'custom':'premium_plan'
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/payment.html',{'form':form})

def update_payment(request):
    # Get the payment table 
    # update the table and the project and order status
    pass

# If cancelled return to payment form