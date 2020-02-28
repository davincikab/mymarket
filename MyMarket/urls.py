from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('market.urls')),
    path('user/',include('user.urls')),
    path('payment',include('payment.urls'))
]

# TODO:
# Implement PassWord Reset

admin.site.site_header = "My Market"
admin.site.site_title = "Market"
admin.site.index_title = "My Market"
