from django.urls import path

from . import views

urlpatterns = [
    # ex: marks/
    path('<int:id>', views.index, name='marks.index'),
    # ex: marks/create
    # path('create', views.create, name='marks.create'),
    # ex: marks/store/
    # path('store', views.store, name='marks.store'),
    # ex: marks/5/
    path('<int:id>/students/<int:idd>', views.student, name='marks.student'),

    # ex: marks/5/edit
    # path('<int:id>/edit', views.edit, name='marks.edit'),
    # ex: marks/5/update
    # path('<int:id>/update', views.update, name='marks.update'),
    # ex: marks/5/delete
    # path('<int:id>/delete', views.delete, name='marks.delete'),
    #update session exam student marks
    path('updatemarksajax', views.updatemarks, name='marks.updatemarks'),
    path('<int:id>/subject/<int:subject>', views.editstudentsubjectmarks, name='marks.subject'),
]