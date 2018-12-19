
from django.urls import path

from . import views

urlpatterns = [
    # ex: studentss/
    path('', views.index, name='medium.index'),
    # ex: studentss/create
    path('create', views.create, name='medium.create'),

    # ex: studentss/store/
    path('store', views.store, name='medium.store'),
    # ex: studentss/5/
    path('<int:id>', views.detail, name='medium.detail'),
    # ex: studentss/5/edit
    path('<int:id>/edit', views.edit, name='medium.edit'),
    # ex: studentss/5/update
    path('<int:id>/update', views.update, name='medium.update'),
    # ex: studentss/5/delete
    # path('<int:id>/delete', views.delete, name='students.delete'),
]