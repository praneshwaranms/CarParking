from parking import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path("",views.location,name="location"),
    path("reg/",views.reg,name="reg"),
    path("registration/",views.registration,name="registration"),
    path("index/",views.home,name="home"),
    path('book_slot/', views.book_slot, name='book_slot'),
    path('booked_view/', views.booked_view, name='booked_view'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup_view/', views.signup_view, name='signup_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('otp_view/', views.otp_view, name='otp_view'),
    path('payment/', views.car_out, name='car_out'),
    path('done/', views.payment_view, name='payment_view'),


]