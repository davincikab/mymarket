from django.db import models
from user.models import User
import uuid

# Create your models here.
class Projects(models.Model):
	project_id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
	created_by = models.OneToOneField(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
	description = models.TextField()
	title = models.CharField(max_length=100)
	timeframe = models.IntegerField("Number of Days")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Project"
		verbose_name_plural = "Projects"

class Orders(models.Model):
	orderid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
	project = models.OneToOneField(Projects, on_delete=models.CASCADE)
	awarded_on = models.DateTimeField(auto_now=True)
	delivery_date = models.DateTimeField(auto_now=False)
	awarded_to = models.OneToOneField(User, on_delete=models.CASCADE)
	isdone = models.BooleanField('Work Completed', default=False)
	isclosed = models.BooleanField("Closed Order", default=False)
	iscanceled = models.BooleanField("Cancel Order", default=False)
	cost = models.IntegerField("Order Cost")


	def __str__(self):
		return self.project.title

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = "Orders"

	# Cutome methods: canceled, closed, delivered in time etc

class Messages(models.Model):
	sender = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user_sender")
	reciever = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_reciever")
	message = models.TextField()
	project = models.OneToOneField(Projects,on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.sender.username

	class Meta:
		verbose_name = "Message"
		verbose_name_plural = "Messages"

	# Custom methods: deal with files (pictures, pdfs)


