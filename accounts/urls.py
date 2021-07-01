from django.urls import path
from . import views
from .views import verification
from django.contrib.auth import views as authviews


urlpatterns = [
    path('verify', views.verify, name='verify'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('update-profile', views.update_profile, name='updateprofile'),
    path('sign-up', views.register, name= 'sign-up'),
    path('activate/<uidb64>/<token>', verification.as_view(), name='activate'),
    path('login/', views.login_view, name='login'),
    path('logout/', authviews.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]