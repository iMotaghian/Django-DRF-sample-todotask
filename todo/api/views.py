from rest_framework import viewsets
from .serializers import TodoSerializer
from ..models import ToDoTask
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class TodoModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = TodoSerializer
    # queryset = ToDoTask.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['user','status']
    ordering_fields = ['created_date']
    
    def get_queryset(self):
        user = self.request.user
        return ToDoTask.objects.filter(user=user)
    
    
    
    