from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='class.index'),
    path('create', views.create, name='class.create'),
    path('store', views.store, name='class.store'),
    path('<int:id>/edit', views.edit, name='class.edit'),
    path('<int:id>/update', views.update, name='class.update'),
    path('<int:id>/delete', views.delete, name='class.delete'),
    path('<int:id>/template', views.template, name='exam.template'),
    path('<int:id>', views.detail, name='class.detail'),
]