from django.db import models

# Create your models here.

class TodoList(models.Model):
    task_title = models.CharField(max_length= 50)
    task_description = models.TextField(max_length= 100)
    completed = models.BooleanField(default=False)


    '''def __str__(self) :
       self.task_title'''



