from django.db import models

# Create your models here.

class TodoApp(models.Model):
    name=models.CharField(max_length=30)
    completed=models.BooleanField(default=False)

    class Meta:
        ordering=["name"]


    def __str__(self):
        return self.name

