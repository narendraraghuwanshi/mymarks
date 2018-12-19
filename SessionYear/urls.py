from django.urls import path

from . import views

urlpatterns = [
    # ex: session/
    path('', views.index, name='session.index'),
    # ex: session/create
    path('create', views.create, name='session.create'),
    # ex: session/store/
    path('store', views.store, name='session.store'),
    # ex: session/5/
    path('<int:id>', views.detail, name='session.detail'),
    # ex: session/5/edit
    path('<int:id>/edit', views.edit, name='session.edit'),
    # ex: session/5/update
    path('<int:id>/update', views.update, name='session.update'),
    # ex: session/5/delete
    path('<int:id>/delete', views.delete, name='session.delete'),
]