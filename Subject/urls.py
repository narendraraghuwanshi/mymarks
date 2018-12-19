
from django.urls import path

from . import views

urlpatterns = [
    # ex: subject/
    path('', views.index, name='subject.index'),
    # ex: subject/create
    path('create', views.create, name='subject.create'),

    # ex: subject/store/
    path('store', views.store, name='subject.store'),
    # ex: subject/5/
    path('<int:id>', views.detail, name='subject.detail'),
    # ex: subject/5/edit
    path('<int:id>/edit', views.edit, name='subject.edit'),
    # ex: subject/5/update
    path('<int:id>/update', views.update, name='subject.update'),
    # ex: subject/5/delete
    path('<int:id>/delete', views.delete, name='students.delete'),
]