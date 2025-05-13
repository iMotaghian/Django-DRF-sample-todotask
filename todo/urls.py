from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('',views.ToDoListView.as_view(), name="todo-listview"),
    path('create/',views.TaskCreateView.as_view(), name="todo-CreateView"),
    path('edit/<int:pk>/',views.ToDoEditView.as_view(), name="todo-UpdateView"),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(), name="todo-DeleteView"),
    path('done/<int:pk>/',views.TaskDone.as_view(), name="todo-TaskDone"),
    path('running/<int:pk>/',views.TaskRun.as_view(), name="todo-TaskRun"),
    path('logout/', views.user_logout, name='logout'),
    path('api/', include('todo.api.urls')),
]