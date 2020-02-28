from django.db import models
from user.models import User
from market.models import Projects,Orders
import uuid

# Create your models here.
class Payment(models.Model):

	PAYMENT = (
		('P','PAYPAL'),
		('MP', 'MPESA')
	)
	payment_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	from_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_payer")
	to_user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_payee")
	amount = models.IntegerField()
	project = models.OneToOneField(Projects, on_delete=models.CASCADE)
	order = models.OneToOneField(Orders, on_delete=models.CASCADE)
	payment_method = models.CharField("Payment Method",choices=PAYMENT,max_length=15)

	def __str__(self):
		return str(self.payment_id)

	class Meta:
		verbose_name = "Payment"
		verbose_name_plural = "Payment"

# Implement a Payment API