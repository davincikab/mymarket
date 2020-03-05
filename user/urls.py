from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateView, UserProfile, MyDashBoard, get_user_profile

urlpatterns = [
	path('login/', LoginView.as_view(template_name='user/login.html'), name="login"),
	path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
	path('register/',UserCreateView.as_view(), name="register"),
	path('profile/', UserProfile.as_view(), name="profile"),
	path('get_user_profile/<int:userid>/',get_user_profile, name="get-user-profile"),
	path('dashboard/',MyDashBoard.as_view(), name='dashboard'),
]
