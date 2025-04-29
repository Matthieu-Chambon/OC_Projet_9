from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.decorators import login_required

from authentication.forms import SignupForm

from reviews.models import Ticket, Review

# rendre la page accessible uniquement aux utilisateurs déconnectés
def signup_page(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

@login_required
def home(request):
    tickets = Ticket.objects.all()
    return render(
        request, 
        'authentication/home.html',
        context={'tickets': tickets,}
    )