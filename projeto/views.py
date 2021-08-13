from django.http import response
from django.shortcuts import redirect, render
from projeto.models import Eventos
# Create your views here.



def lista_checagem(request):
    eventos = Eventos.objects.all()
    dados = {'eventos': eventos}
    return render(request, 'base.html', dados)

def tarefas(request):
    return render(request, 'tarefas.html')

def submit_tarefas(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        nome = request.POST.get('nome')
        data_inicio = request.POST.get('data_inicio')
        info = request.POST.get('info')
        usuario = request.user
        Eventos.objects.create(titulo=titulo, nome=nome, data_inicio=data_inicio, info=info,
            usuario=usuario)
    return redirect('/')

def delete_eventos(request, id_eventos):
    usuario = request.user
    eventos = Eventos.objects.get(id=id_eventos)
    if usuario == eventos.usuario:
        eventos.delete()
    return redirect('/')