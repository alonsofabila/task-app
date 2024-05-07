from django.db import models
from task_app.apps.users.functions import generate_custom_uuid
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):
    """
    Tasks model
    """

    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Done')
    ]

    id = models.CharField(max_length=15, primary_key=True, default=generate_custom_uuid('task'), editable=False)
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(blank=True, verbose_name='Contenido')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Creado por")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
