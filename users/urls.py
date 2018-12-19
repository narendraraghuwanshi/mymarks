
from django.urls import path

from . import views

urlpatterns = [
    # ex: users/
    path('', views.index, name='user.index'),
    # ex: users/create
    path('create', views.create, name='user.create'),
    # ex: users/store/
    path('store', views.store, name='user.store'),
    # ex: users/5/
    path('<int:id>', views.detail, name='user.detail'),
    # ex: users/5/edit
    path('<int:id>/edit', views.edit, name='user.edit'),
    # ex: users/5/update
    path('<int:id>/update', views.update, name='user.update'),
    # ex: users/5/delete
    path('<int:id>/delete', views.delete, name='user.delete'),
]