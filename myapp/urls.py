from django.urls import path
from myapp import views
from myapp.Signup import signup_view



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', signup_view, name='signup'),
]
