from django.contrib import admin
from task.models import Category
from task.models import TaskList
# Register your models here.


admin.site.register(Category)
admin.site.register(TaskList)
