from django.db import models

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(
        max_length=100, help_text='Obrigatório preencher o todo')
    done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.todo
