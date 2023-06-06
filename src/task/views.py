from django.shortcuts import render
from task.models import Category
from task.models import TaskList
from task.forms import TaskCreateFrom
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect
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
    return render(request, 'task/index.html', dic)


class TaskDetail(DetailView):
    model = TaskList
    template_name = 'task/detail.html'


def delete_task(request, id):
    task = get_object_or_404(TaskList, id=id)
    task.delete()
    return redirect('show_task')
