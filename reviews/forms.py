from django import forms

from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'aria-label': 'Titre du billet',
                'aria-required': 'true',
                'required': 'required',
            }),
            'description': forms.Textarea(attrs={
                'rows': 20,
                'aria-label': 'Description du billet',
                'aria-required': 'true',
                'required': 'required',
            }),
            'image': forms.ClearableFileInput(attrs={
                'aria-label': 'Image du billet',
                'aria-required': 'false',
            }),
        }
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={
                'aria-label': 'Titre de la critique',
                'aria-required': 'true',
                'required': 'required',
            }),
            'rating': forms.Select(attrs={
                'aria-label': 'Note de la critique',
                'aria-required': 'true',
                'required': 'required',
            }),
            'body': forms.Textarea(attrs={
                'rows': 20,
                'aria-label': 'Commentaire de la critique',
                'aria-required': 'true',
                'required': 'required',
            }),
        }
        labels = {
            'rating': 'Note',
            'headline': 'Titre',
            'body': 'Commentaire',
        }


class TicketAndReviewForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticket = TicketForm(*args, **kwargs)
        self.review = ReviewForm(*args, **kwargs)

    def is_valid(self):
        return self.ticket.is_valid() and self.review.is_valid()

    def save(self, user):
        ticket = self.ticket.save(commit=False)
        ticket.user = user
        ticket.save()

        review = self.review.save(commit=False)
        review.ticket = ticket
        review.user = user
        review.save()

        return ticket, review
