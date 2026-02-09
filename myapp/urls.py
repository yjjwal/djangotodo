from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    # done task
    path('task_is_done/<int:pk>/',views.task_is_done,name='task_is_done'),
    # undone task
    path('task_is_undone/<int:pk>/',views.task_is_undone,name='task_is_undone'),
    # edit task
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    # delete task
    path('delete_task/<int:pk>',views.delete_task,name='delete_task')

]

