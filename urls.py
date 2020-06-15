from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'), # this is for home
     path('login/', views.login), # this is for login panel
    path('administration/', views.administration), # this is for admin panel
    path('registration/', views.registration), # this is for registration now you have to add for login/
    path('new_member/', views.new_member),
    path('forgot_password/', views.forgot_password),
    path('change_password/', views.change_password),


    # these whole functions
]
