from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from reviews.models import Ticket, Review
from reviews.forms import TicketForm, ReviewForm, TicketAndReviewForm

###################### My posts ######################

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
    
    # ne garder que les tickets et les reviews de l'utilisateur connecté
    items = [*tickets , *reviews]
    items.sort(key=lambda x: x.time_created, reverse=True)
       
    return render(
        request, 
        'reviews/my_posts.html',
        context={'items': items}
    )

###################### Tickets ######################

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
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'reviews/ticket_details.html', {'ticket': ticket})

@login_required
def ticket_edit(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    if request.user != ticket.user:
        return redirect('ticket-details', ticket_id=ticket.id)
    
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        
        if form.is_valid():
            form.save()
            return redirect('ticket-details', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)
        
    return render(request, 'reviews/ticket_edit.html', {'form': form, 'ticket': ticket})

@login_required
def ticket_delete(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    if request.user != ticket.user:
        return redirect('ticket-details', ticket_id=ticket.id)
    
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    
    return render(request, 'reviews/ticket_delete.html', {'ticket': ticket})

####################### Reviews ######################

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
            return redirect('ticket-details', ticket_id=ticket.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_create.html', {'form': form, 'ticket': ticket})

@login_required
def review_edit(request, review_id):
    review = Review.objects.get(id=review_id)
    ticket = Ticket.objects.get(id=review.ticket.id)
    
    if request.user != review.user:
        return redirect('home')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm(instance=review)
        
    return render(request, 'reviews/review_edit.html', {'form': form, 'ticket': ticket})

@login_required
def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    
    if request.user != review.user:
        return redirect('home')
    
    if request.method == 'POST':
        review.delete()
        return redirect('ticket-details', ticket_id=review.ticket.id)
    
    return render(request, 'reviews/review_delete.html', {'review': review})

@login_required
def create_ticket_and_review(request):
    if request.method == 'POST':
        print("POST request received")
        print(request.POST)
        form = TicketAndReviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("Form is valid")
            ticket, review = form.save(user=request.user)
            return redirect('ticket-details', ticket_id=ticket.id)
    else:
        form = TicketAndReviewForm()
        
    return render(request, 'reviews/ticket_and_review_create.html', {'form': form})