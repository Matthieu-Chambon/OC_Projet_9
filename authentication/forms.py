from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User, UserFollows


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'aria-label': 'Nom d\'utilisateur',
                'aria-required': 'true',
                'required': 'required',
            }),
            'password1': forms.PasswordInput(attrs={
                'aria-label': 'Mot de passe',
                'aria-required': 'true',
                'required': 'required',
            }),
            'password2': forms.PasswordInput(attrs={
                'aria-label': 'Confirmer le mot de passe',
                'aria-required': 'true',
                'required': 'required',
            }),
        }


class SubscribeForm(forms.ModelForm):
    followed_user = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Rechercher un utilisateur...',
            'aria-label': 'Nom d\'utilisateur à suivre',
            'aria-required': 'true',
            'required': 'required',
        }),
    )

    class Meta:
        model = UserFollows
        fields = ('followed_user',)
        labels = {
            'followed_user': 'Nom d\'utilisateur à suivre',
        }

    def clean_followed_user(self):
        username = self.cleaned_data['followed_user']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Aucun utilisateur avec ce nom n'existe.")
        return user


class UnsubscribeForm(forms.Form):
    unfollow_user_id = forms.IntegerField(widget=forms.HiddenInput)
