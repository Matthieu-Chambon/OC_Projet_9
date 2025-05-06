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


class SubscribeForm(forms.ModelForm):
    followed_user = forms.CharField(max_length=150)

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
