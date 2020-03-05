from django.shortcuts import get_object_404
from .models import Orders
from paypal.standard.ipn.signals import valid_ipn_recieved
from django.dispatch import reciever

@reciever(valid_ipn_recieved):
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        order = get_object_404(Orders, orderid=ipn.invoice)
        print(ipn)
        if order.cost == ipn.mc_gross:
            order.isclosed = True
            order.isdone = True
            order.save()