from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from .models import Entrepot, Adresse
from .forms import EntrepotForm, AdresseForm


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


@csrf_protect
@login_required(login_url='/login')
def entrepot_listing(request):
    """
        Listings des entrepots
        Pas de gestion de la pagination
        :param request
        :return: entrepot/entrepots.html avec un les donnees de la requete entrepots
        """
    entrepots = Entrepot.objects.filter(entreprise=settings.ENTREPRISE)
    return render(request,
                  'entrepot/entrepots.html',
                  {"entrepots": entrepots})


@csrf_protect
@login_required(login_url='/login')
def create_entrepot(request):
    if request.method == 'POST':
        adresse_form = AdresseForm(request.POST, prefix='adr')
        entrepot_form = EntrepotForm(request.POST, prefix='ent')
        if adresse_form.is_valid() and entrepot_form.is_valid():
            adr = adresse_form.save()
            ent = entrepot_form.save(commit=False)
            ent.adresse = adr
            ent.save()
            return redirect('entrepot-listing')
    else:
        adresse_form = AdresseForm(prefix='adr')
        entrepot_form = EntrepotForm(prefix='ent')

    return render(request, 'entrepot/entrepot_form.html', {
        'adresse_form': adresse_form,
        'entrepot_form': entrepot_form,
    })
