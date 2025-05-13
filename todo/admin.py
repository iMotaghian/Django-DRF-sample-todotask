from django.contrib import admin
from .models import ToDoTask

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'status','created_date','updated_date']


admin.site.register(ToDoTask,TaskAdmin)