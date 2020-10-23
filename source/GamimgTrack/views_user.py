from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, ChangeUserPasswordForm, ChangeUserEmailForm, ChangeUserNameForm
from django.http import JsonResponse

from GamimgTrack.models import User

### Setando strings: 
IrParaLogin = "user/login.html"
IrParaRegistrar = "user/register.html"
IrParaInfo = "user/info.html"
IrParaAlterar = "user/alterar.html"
IrParaListarUsers = "user/lista_users.html"
IrParaVisita = "user/visitar_outro.html"
MensagemErro = "Algo de errado não está certo"
IrParaInicio = "inicio.html"

def RegisterUser(response):
    if response.method == "POST":
        form = RegisterUserForm(response.POST)

        if form.is_valid():
            #create(first_name="Bruce", last_name="Springsteen")
            n = form.cleaned_data["nome"] # n recebe o nome do usuario
            em = form.cleaned_data["email"]
            lo = form.cleaned_data["login"]
            p = form.cleaned_data["password"]
            p1 = form.cleaned_data["password1"]
            if p != p1:
                return JsonResponse(data = {"message": "Erro: Senhas diferentes"})
            if User.objects.filter(login=lo).count() == 0:
                User.objects.create(email=em, login=lo, password=p, nome=n)
                form = LoginUserForm()
                return render(response, IrParaLogin, {"form":form})
            else:
                return JsonResponse(data = {"message": "E-mail já registrado no site"})

    else:
        form = RegisterUserForm()
        return render(response, IrParaRegistrar, {"form":form})
def LoginUser(response):
    
    if response.method == "POST":
        form = LoginUserForm(response.POST)

        if form.is_valid():
            lo = form.cleaned_data["login"]
            p = form.cleaned_data["password"]
            if User.objects.filter(login=lo).count() == 0:
                    return JsonResponse(data = {"message": "E-mail não registrado no site"})
            if User.objects.filter(login=lo, password=p).count() == 0:
                return JsonResponse(data = {"message": "Login ou senha incorretos"})
            else:
                logado = User.objects.get(login=lo, password=p)
                response.session['id_user'] = logado.id
                return render(response, IrParaInicio, {"user":logado})
    else:
        form = LoginUserForm()
        return render(response, IrParaLogin, {"form":form})

def mostrar_detalhes(response):
    logado = User.objects.get(id = response.session['id_user'])
    return render(response, IrParaInfo, {"user":logado})

def AlterarSenhaUser(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserPasswordForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            p1 = form.cleaned_data["password1"]
            p2 = form.cleaned_data["password2"]
            if (logado.password == p2) and (p == p1):
                logado.password = p
                logado.save()
                return render(response, IrParaInfo, {"user":logado})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserPasswordForm()
        return render(response, IrParaAlterar, {"form":form})

def AlterarNomeUser(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserNameForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data['nome']
            p = form.cleaned_data['password']
            if (logado.password == p):
                logado.nome = n
                logado.save()
                return render(response, IrParaInfo, {"user":logado})
            else:
                return JsonResponse(data = {"message": "Senha incorreta"})
    else:
        form = ChangeUserNameForm()
        return render(response, IrParaAlterar, {"form":form})

def AlterarLoginUser(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserEmailForm(response.POST)

        if form.is_valid():
            p = form.cleaned_data["password"]
            e = form.cleaned_data['email']
            if (logado.password == p):
                logado.email = e
                logado.save()
                return render(response, IrParaInfo, {"user":logado})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserEmailForm()
        return render(response, IrParaAlterar, {"form":form})

def DeletarMinhaConta(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == "POST":
        form = ChangeUserEmailForm(response.POST)

        if form.is_valid():
            em = form.cleaned_data["email"]
            p = form.cleaned_data["password"]
            if (logado.password == p) and (logado.email == em):
                logado.delete()
                form = LoginUserForm()
                return render(response, IrParaLogin, {"form":form})
            else:
                return JsonResponse(data = {"message": MensagemErro})
    else:
        form = ChangeUserEmailForm()
        return render(response, IrParaAlterar, {"form":form})

def ListarUsuarios(response):
    logado = User.objects.get(id = response.session['id_user'])
    if response.method == 'POST':
        # Verifica se foi apertado um botão para upgradar alguma conta
        upgradar = ["Comum", '',"Tutor", "Moderador", "Administrador"] # Lista para os botões de upgrade
        NivelPermissao = 1
        for k in upgradar:
            if k in response.POST:
                ContaParaUpgradar = User.objects.get(id = response.session['id_visita'])
                if logado.permissionlevel >= NivelPermissao and ContaParaUpgradar.permissionlevel <= logado.permissionlevel:
                    ContaParaUpgradar.permissionlevel = NivelPermissao
                    ContaParaUpgradar.save()
                    return render(response, IrParaVisita, {"user":logado, "visita":ContaParaUpgradar, "upgradar": upgradar})
            NivelPermissao+=1
        
        # Verifica se o botão pressionado foi o botão de Pesquisar
        if "pesquisar" in response.POST:
            lista = []
            filtro = response.POST.get('filtro')
            for users in User.objects.exclude(id = response.session['id_user']).filter(nome__contains=filtro):
                sla = []
                sla.append(users.nome)
                sla.append(users.id)
                lista.append(sla)
                # Ele filtra pela pesquisa por nome
            return render(response, IrParaListarUsers, {'lista': lista})
        for i in User.objects.exclude(id = response.session['id_user']):
            if str(i.id) in response.POST:
                # Aqui ele verifica se o botão pressionado tem o id do user no select
                visitar = i
                response.session['id_visita'] = visitar.id
                return render(response, IrParaVisita, {"user":logado, "visita":visitar, "upgradar": upgradar})
        
        return JsonResponse(data = {"message": MensagemErro})
    else:
        lista = []
        for users in User.objects.exclude(id = response.session['id_user']):
            sla = []
            sla.append(users.nome)
            sla.append(users.id)
            lista.append(sla)
            #lista recebe uma lista que possue sempre 2 valores, o primeiro é o nome do usuario e o segundo o seu id, que ficará no nome do botão
        return render(response, IrParaListarUsers, {'lista': lista})

def ApagarOutraConta(response):
    # Adm pode apagar uma conta de outro usuario
    logado = User.objects.get(id = response.session['id_user'])
    ContaParaDeletar = User.objects.get(id = response.session['id_visita'])
    if logado.permissionlevel >= 4 and ContaParaDeletar.permissionlevel <= logado.permissionlevel:
        ContaParaDeletar.delete()
        response.session['id_visita'] = ''
        return render(response, IrParaInicio, {"user":logado})
    else:
        return JsonResponse(data = {"message": MensagemErro})