from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms_postagens import CriarPostagemForm
from .models import Postagem, User, ComentariosPostagens
from .views_user import IrParaVisita, IrParaInicio, verificar_amizade
from .views_comentarios import pegar_comentarios_Postagens

MensagemErro = "Algo de errado não está certo"
criar_postagem = "posts/criar_post.html"
IrParaListarPostagens = "posts/lista_postagens.html"
ver_postagem = "inicio.html"
IrParaInfo = "user/info.html"


def criar_nova_postagem(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == "POST":
        title = response.POST.get("title")
        content = response.POST.get("content")
        post = Postagem.objects.create(title=title, content=content,
                                       user_criador=logado)
        post.save()
        return render(response, ver_postagem, {"user": logado, "post": post, "criador": post.user_criador, "lista_comentarios":None, "lista_de_postagens":pegar_lista_de_postagens()})
    else:
        form = CriarPostagemForm()
        return render(response, criar_postagem, {"form": form})


def listar_postagens(response):
    logado = User.objects.get(id=response.session['id_user'])
    if response.method == 'POST':
        if "visitar" in response.POST:
            visitar = Postagem.objects.get(id=response.session['id_postagem']).user_criador
            if visitar == logado:
                return render(response, IrParaInfo, {"user":logado})
            upgradar = ["Comum", '', "Tutor", "Moderador", "Administrador"]
            return render(response, IrParaVisita, {"user": logado, "visita": visitar, "upgradar": upgradar, "amizade": verificar_amizade(logado, ContaParaUpgradar)})
        elif "apagar" in response.POST:
            p = Postagem.objects.get(id=response.session['id_postagem'])
            p.delete()
            return render(response, IrParaInicio, {"user": logado})
        # Verifica se o botão pressionado foi o botão de Pesquisar
        elif "pesquisar" in response.POST:
            lista = []
            filtro = response.POST.get('filtro')
            for posts in Postagem.objects.filter(title__contains=filtro):
                sla = []
                sla.append(posts.title)
                sla.append(posts.id)
                lista.append(sla)
                # Ele filtra pela pesquisa por nome
            return render(response, IrParaListarPostagens, {'lista': lista})
        elif "comentar" in response.POST:
            visitar = Postagem.objects.get(id=response.session['id_postagem'])
            ComentariosPostagens.objects.create(postagem=visitar, user=logado, comentario=response.POST.get('comentario')).save()
            comentarios = pegar_comentarios_Postagens(visitar.id)
            return render(response, ver_postagem, {"user":logado, "post":visitar, "lista_comentarios":comentarios})
        for i in Postagem.objects.all():
            if str(i.id) in response.POST:
                # Aqui ele verifica se o botão pressionado tem o id do user no select
                visitar = i
                response.session['id_postagem'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios_Postagens(visitar.id)
                return render(response, ver_postagem, {"user": logado, "post": visitar, "criador": criador, "lista_comentarios":comentarios})
        return JsonResponse(data={"message": MensagemErro})
    else:
        lista = []
        filtro = response.POST.get('filtro')
        for posts in Postagem.objects.all():
            sla = []
            sla.append(posts.title)
            sla.append(posts.id)
            lista.append(sla)
            # Ele filtra pela pesquisa por nome
        return render(response, IrParaListarPostagens, {'lista': lista})

def mostrar_posts_visita(response):
    visita = User.objects.get(id = response.session['id_visita'])
    lista = []
    if response.method == "POST":
        for i in Postagem.objects.all():
            if str(i.id) in response.POST:
                # Aqui ele verifica se o botão pressionado tem o id do user no select
                visitar = i
                response.session['id_postagem'] = visitar.id
                criador = visitar.user_criador
                comentarios = pegar_comentarios_Postagens(visitar.id)
                return render(response, ver_postagem, {"user":visita, "post":visitar, "criador": criador, "lista_comentarios":comentarios})
        filtro = response.POST.get('filtro')
        for posts in Postagem.objects.filter(user_criador = visita, title__contains=filtro):
            sla = []
            sla.append(posts.title)
            sla.append(posts.id)
            lista.append(sla)
        return render(response, IrParaListarPostagens, {'lista': lista})
    for posts in Postagem.objects.filter(user_criador = visita):
        sla = []
        sla.append(posts.title)
        sla.append(posts.id)
        lista.append(sla)
    return render(response, IrParaListarPostagens, {'lista': lista})

def pegar_lista_de_postagens():
    lista = []
    for posts in Postagem.objects.all():
        sla = []
        sla.append(posts.title)
        sla.append(posts.id)
        lista.append(sla)
    return lista