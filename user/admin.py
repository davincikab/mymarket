from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Certification, Academic, Profile,Skill

# Register your models here.;
admin.site.register(User,UserAdmin)
admin.site.register(Certification)
admin.site.register(Academic)
admin.site.register(Skill)
admin.site.register(Profile)

