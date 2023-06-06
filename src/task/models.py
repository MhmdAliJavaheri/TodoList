from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TaskList(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now())
    category = models.ForeignKey(
        Category, default='Genral', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
