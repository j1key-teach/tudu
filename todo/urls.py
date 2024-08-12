from django.urls import path
from .views import TodoList, TodoCreate, TodoRetrieve, TodoUpdate, TodoDelete

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/create/', TodoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/', TodoRetrieve.as_view(), name='todo-retrieve'),
    path('todos/<int:pk>/update/', TodoUpdate.as_view(), name='todo-update'),
    path('todos/<int:pk>/delete/', TodoDelete.as_view(), name='todo-delete'),
]
