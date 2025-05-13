from django.shortcuts import render
from django.contrib.auth import logout
from .models import ToDoTask
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from .forms import EditForm,TaskForm
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
class ToDoListView(LoginRequiredMixin,ListView):
    model = ToDoTask
    context_object_name = "tasks"
    paginate_by = 10
    ordering ='-id'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = ToDoTask
    form_class = TaskForm
    success_url = "/"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ToDoEditView(LoginRequiredMixin,UpdateView):
    model = ToDoTask
    form_class = EditForm
    success_url = "/"
    
class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = ToDoTask
    success_url = "/"
    
    
class TaskDone(LoginRequiredMixin,View):
    model = ToDoTask
    success_url = "/"

    def get(self, request, *args, **kwargs):
        object = ToDoTask.objects.get(id=kwargs.get("pk"))
        object.status = 'done'
        object.save()
        return redirect(self.success_url)
    
class TaskRun(LoginRequiredMixin,View):
    model = ToDoTask
    success_url = "/"

    def get(self, request, *args, **kwargs):
        object = ToDoTask.objects.get(id=kwargs.get("pk"))
        object.status = 'running'
        object.save()
        return redirect(self.success_url)
    
    
    
def user_logout(request):
    logout(request)
    return redirect('/')