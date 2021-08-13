from projeto.models import Eventos
from django.contrib import admin
from .models import Eventos

# Register your models here.

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'nome', 'data_inicio', 'data_termino')
    list_filter = ('usuario', 'data_inicio',)

