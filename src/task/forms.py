from django import forms
from task.models import TaskList


class TaskCreateFrom(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('title', 'created', 'category')
