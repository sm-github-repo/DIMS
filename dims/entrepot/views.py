from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

@csrf_protect
@login_required(login_url='/login')
def tbd(request):
    return render(request, 'entrepot/index.html', {})

@csrf_protect
@login_required(login_url='/login')
def index(request):
    return render(request, 'entrepot/entrepot.html', {})

@csrf_protect
def user_login(request):
    """
       Validation du formulaire de login et redirige l'utilisateur vers la bonne page
       :param request:
       :return: si NOK renvoie vers la page login.html avec code Erreur sinon redirige vers le listing articles
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('entrepot-tbd')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'entrepot/login.html', {'login_erreur': 'Erreur de login'})
    return render(request, 'entrepot/login.html')


@csrf_protect
@login_required(login_url='/login')
def user_logout(request):
    """

    :param request:
    :return: rendu de la page de deconnexion, renvoie à la page login
    """
    logout(request)
    return redirect('login')


