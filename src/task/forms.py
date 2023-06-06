from django import forms
from task.models import TaskList


class DataInput(forms.DataInput):
    input_type = 'date'


class TaskCreateFrom(forms.ModelForm):
    created = forms.DateField(widget=DataInput)

    class Meta:
        model = TaskList
        fields = ('title', 'created', 'category')
