from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
    data_inicio = models.DateTimeField(auto_now_add=True, verbose_name="Check-in")
    data_termino = models.DateTimeField(auto_now=True, verbose_name="Check-out")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'agendamento'

    def __str__(self):
        return self.titulo
    
    def get_data_inicio(self):
        return self.data_inicio.strftime('%d/%m/%Y %H:%M')
