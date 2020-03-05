from django.contrib import admin
from .models import Projects, Orders, Messages

# Register your models here.
admin.site.register(Projects)
admin.site.register(Orders)
admin.site.register(Messages)
