from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dashboard.index'),
    # path('create', views.create, name='create'),
    # path('store', views.store, name='store'),
    # path('<int:id>/edit', views.edit, name='edit'),
    # path('<int:id>/update', views.update, name='update'),
    # path('<int:id>/delete', views.delete, name='delete'),

]