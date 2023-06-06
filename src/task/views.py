from django.shortcuts import render
from task.models import Category
from task.models import TaskList
from task.forms import TaskCreateFrom
from django.http import HttpResponseRedirect
# Create your views here.


def show_task(request):
    query = TaskList.objects.all().order_by('created')

    form = TaskCreateFrom(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = TaskCreateFrom()

    dic = {
        'query': query,
        'form': form,
    }
    return render(request, 'index.html', dic)
