from django.urls import path
from . import views

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    path('toggle_complete/<int:task_id>', views.toggle_complete, name='toggle_complete'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('completed/', views.completed, name='completed'),
    path('all/', views.all, name='all'),

] 

