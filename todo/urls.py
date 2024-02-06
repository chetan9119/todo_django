from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_Done/<int:pk>/', views.mark_as_Done, name='mark_as_Done'),
    
    path('mark_as_Undone/<int:pk>/', views.mark_as_Undone, name='mark_as_Undone'),
    path('edit_Task/<int:pk>/', views.edit_Task, name='edit_Task'),
    path('removeTask/<int:pk>/', views.removeTask, name='removeTask'),
]