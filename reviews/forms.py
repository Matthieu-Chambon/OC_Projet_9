from django import forms

from reviews.models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 20}),
            # 'image': forms.ClearableFileInput(attrs={'class': 'image-input'}),
        }
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }
