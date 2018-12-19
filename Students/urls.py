from django.urls import path

from . import views

urlpatterns = [
    # ex: studentss/
    path('', views.index, name='students.index'),
    # ex: studentss/create
    path('create', views.create, name='students.create'),
    # ex: studentss/countries
    path('countries', views.countries, name='students.countries'),
    # ex: studentss/states
    path('states', views.states, name='students.states'),
    # ex: studentss/store/
    path('store', views.store, name='students.store'),
    # ex: studentss/5/
    path('<int:id>', views.detail, name='students.detail'),
    # ex: studentss/5/edit
    path('<int:id>/edit', views.edit, name='students.edit'),
    # ex: studentss/5/update
    path('<int:id>/update', views.update, name='students.update'),
    # ex: studentss/5/delete
    path('<int:id>/delete', views.delete, name='students.delete'),

    # ex: studentss/5/delete
    path('excel', views.excel, name='students.excel'),

]