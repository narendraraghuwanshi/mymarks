
from django.urls import path

from . import views

urlpatterns = [
    # ex: exam/
    path('', views.index, name='exam.index'),
    # ex: exam/create
    path('create', views.create, name='exam.create'),

    # ex: exam/store/
    path('store', views.store, name='exam.store'),
    # ex: exam/5/
    path('<int:id>/detail', views.detail, name='exam.detail'),
    # ex: exam/5/
    path('<int:id>/subject', views.subject, name='exam.subject'),
    # ex: exam/5/edit
    path('<int:id>/edit', views.edit, name='exam.edit'),
    # ex: exam/5/update
    path('<int:id>/update', views.update, name='exam.update'),
    # ex: exam/5/delete
    path('<int:id>/delete', views.delete, name='exam.delete'),
]