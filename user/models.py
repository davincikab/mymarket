from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group 
from PIL import Image

# Create your models here.
class User(AbstractUser):
	middle_name = models.CharField("Middle Name", max_length=50, blank=True)

	class Meta:
		verbose_name = "User"

class Skill(models.Model):

	INDUSTRY = (
		("PT","Programming and Tech"),
		("DD","Databases Design"),
		("WF","Welding and Fabrication"),
		("CL","Cleaning and LandScaping"),
		("MW","Mechanic Work"),
		("ID","Interior Design"),
	)

	name = models.CharField(max_length=80)
	category = models.CharField(choices=INDUSTRY, max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Skill"
		verbose_name_plural = "Skills"

# TODO: Auto populate with 	
class Profile(models.Model):
	GENDER = (
		('M','Male'),
		('F','Female'),
		('O','Others')
	)

	INDUSTRY = (
		("PT","Programming and Tech"),
		("DD","Databases Design"),
		("WF","Welding and Fabrication"),
		("CL","Cleaning and LandScaping"),
		("MW","Mechanic Work"),
		("ID","Interior Design"),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_of_birth = models.DateField(auto_now=False)
	gender = models.CharField(choices=GENDER, max_length=8)
	profile_picture = models.FileField(upload_to="profile_pic", default="")
	industry = models.CharField(max_length=100,choices=INDUSTRY)
	skills = models.ManyToManyField(Skill)
	description = models.TextField()
	phone_number = models.CharField("Phone Number",max_length=15, blank=True, default="+254740368934")

	class Meta:
		verbose_name = "User Profile"
		verbose_name_plural = "User Profile"

	def __str__(self):
		return self.user.username

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		image = Image.open(self.profile_picture.path)

		if image.height>300 and image.width>300:
			output_size = (100,100)
			image.thumbnail(output_size)
			image.save(self.profile_picture.path)


class Academic(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	institution = models.CharField(max_length=255)
	level = models.CharField(max_length=15)
	start_date = models.DateField(auto_now=False)
	end_date = models.DateField(auto_now=False)
	awarded = models.CharField(max_length=255)


	class Meta:
		verbose_name = "Academic Information"
		verbose_name_plural ="Academic Information"

	def __str__(self):
		return f'{self.user} {self.awarded}'

class Certification(models.Model):
	"""
	Certification class to deal with 
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	organization = models.CharField("Institution/Organization",max_length=255)
	date = models.DateField()

	class Meta:
		verbose_name = "Certification"
		verbose_name_plural = "Certifications"

	def __str__():
		return f'{self.user} {self.name}'
		
	# Other custom methods


# TODO: Choice Field with choices (single or multiple)
# Save while Editing: Cater for Network issues, is_draft

