
from django.urls import path

from . import views

urlpatterns = [
    # ex: users/
    path('', views.index, name='login'),
    # ex: users/
    path('check', views.check, name='login.check'),
    # ex: users/logout
    path('logout', views.logoutuser, name='logout'),

]