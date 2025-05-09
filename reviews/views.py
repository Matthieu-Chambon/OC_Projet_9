from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authentication.forms import SubscribeForm, UnsubscribeForm
from authentication.models import User, UserFollows

from reviews.models import Ticket, Review
from reviews.forms import TicketForm, ReviewForm, TicketAndReviewForm

from django.db.models import Q


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


@login_required
def my_posts(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    tickets = tickets.filter(user=request.user)
    reviews = reviews.filter(user=request.user)

    for ticket in tickets:
        ticket.type = 'ticket'

    for review in reviews:
        review.type = 'review'

    items = [*tickets, *reviews]
    items.sort(key=lambda x: x.time_created, reverse=True)

    return render(
        request,
        'reviews/my_posts.html',
        context={'items': items}
    )


@login_required
def subscriptions(request):
    if request.method == 'POST':

        if request.POST.get('action') == 'subscribe':

            subscribe_form = SubscribeForm(request.POST)
            unsubscribe_form = UnsubscribeForm()

            if subscribe_form.is_valid():
                followed_user = subscribe_form.cleaned_data['followed_user']

                if followed_user != request.user:

                    if UserFollows.objects.filter(user=request.user, followed_user=followed_user).exists():
                        subscribe_form.add_error('followed_user', "Vous suivez déjà cet utilisateur.")

                    else:
                        user_follows = UserFollows.objects.create(
                            user=request.user,
                            followed_user=followed_user
                        )
                        user_follows.save()
                        subscribe_form = SubscribeForm()

                else:
                    subscribe_form.add_error('followed_user', "Vous ne pouvez pas vous abonner à vous-même.")

        elif request.POST.get('action') == 'unsubscribe':

            subscribe_form = SubscribeForm()
            unsubscribe_form = UnsubscribeForm(request.POST)

            if unsubscribe_form.is_valid():
                unfollowed_user_id = unsubscribe_form.cleaned_data['unfollow_user_id']
                unfollowed_user = User.objects.get(id=unfollowed_user_id)
                user_follows = UserFollows.objects.filter(user=request.user, followed_user=unfollowed_user)
                user_follows.delete()

    else:
        subscribe_form = SubscribeForm()
        unsubscribe_form = UnsubscribeForm()

    user_follows_list = UserFollows.objects.filter(user=request.user)
    users_followed = [user_follows.followed_user for user_follows in user_follows_list]

    user_follows_list = UserFollows.objects.filter(followed_user=request.user)
    followers = [user_follows.user for user_follows in user_follows_list]

    return render(
        request,
        'reviews/subscriptions.html',
        {
            'subscribe_form': subscribe_form,
            'unsubscribe_form': unsubscribe_form,
            'users_followed': users_followed,
            'followers': followers,
        }
    )


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'reviews/ticket_create.html', {'form': form})


@login_required
def ticket_edit(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.user != ticket.user:
        return redirect('home')

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'reviews/ticket_edit.html', {'form': form, 'ticket': ticket})


@login_required
def ticket_delete(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.user != ticket.user:
        return redirect('home')

    if request.method == 'POST':
        ticket.delete()
        return redirect('my-posts')

    return render(request, 'reviews/ticket_delete.html', {'ticket': ticket})


@login_required
def review_create(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if ticket.answered:
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('my-posts')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_create.html', {'form': form, 'ticket': ticket})


@login_required
def review_edit(request, review_id):
    review = Review.objects.get(id=review_id)
    ticket = Ticket.objects.get(id=review.ticket.id)

    if request.user != review.user:
        return redirect('my-posts')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('my-posts')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_edit.html', {'form': form, 'ticket': ticket})


@login_required
def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)

    if request.user != review.user:
        return redirect('my-posts')

    if request.method == 'POST':
        review.delete()
        return redirect('my-posts')

    return render(request, 'reviews/review_delete.html', {'review': review})


@login_required
def create_ticket_and_review(request):
    if request.method == 'POST':
        form = TicketAndReviewForm(request.POST, request.FILES)

        if form.is_valid():
            ticket, review = form.save(user=request.user)
            return redirect('my-posts')
    else:
        form = TicketAndReviewForm()

    return render(request, 'reviews/ticket_and_review_create.html', {'form': form})
