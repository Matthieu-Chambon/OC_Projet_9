from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from reviews.models import Ticket, Review
from reviews.forms import TicketForm


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