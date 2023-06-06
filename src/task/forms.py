from django import forms
from task.models import TaskList


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskCreateFrom(forms.ModelForm):
    created = forms.DateField(widget=DateInput)

    class Meta:
        model = TaskList
        fields = ('title', 'created', 'category')
