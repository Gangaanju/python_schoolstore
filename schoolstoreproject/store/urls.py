
from django.urls import path
from . import views
app_name = 'store'


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', views.logout, name='logout'),
    path('submit_form/', views.submit_form, name='submit_form'),




]
