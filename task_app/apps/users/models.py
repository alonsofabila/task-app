from django.db import models
from task_app.apps.users.functions import generate_custom_uuid


# Create your models here.
class User(models.Model):
    """
    User model
    """
    id = models.CharField(max_length=15, primary_key=True, default=generate_custom_uuid('user'), editable=False)
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    username = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    email = models.EmailField(unique=True, verbose_name='Correo electronico')
    password = models.CharField(max_length=50, verbose_name='Contraseña')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    def __str__(self):
        return f'{self.username}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
