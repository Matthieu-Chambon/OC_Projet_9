from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.decorators import login_required

from authentication.models import UserFollows
from authentication.forms import SignupForm

from reviews.models import Ticket, Review

from django.db.models import Q


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
    reviews = Review.objects.all()

    user_follows_list = UserFollows.objects.filter(user=request.user)
    users_followed = [user_follows.followed_user for user_follows in user_follows_list]

    tickets = tickets.filter(Q(user=request.user) | Q(user__in=users_followed))
    reviews = reviews.filter(Q(user=request.user) | Q(ticket__user=request.user))

    for ticket in tickets:
        ticket.type = 'ticket'

    for review in reviews:
        review.type = 'review'

    items = [*tickets, *reviews]
    items.sort(key=lambda x: x.time_created, reverse=True)

    return render(
        request,
        'authentication/home.html',
        context={'items': items}
    )
