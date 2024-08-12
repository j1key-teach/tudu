from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


# View for listing to-dos (GET)
class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# View for creating a to-do (POST)
class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# View for retrieving a single to-do (GET)
class TodoRetrieve(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# View for updating a to-do (PUT/PATCH)
class TodoUpdate(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# View for deleting a to-do (DELETE)
class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
