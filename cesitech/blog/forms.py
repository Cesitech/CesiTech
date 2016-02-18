from django import forms
from models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('sujet','envoyeur', 'message',)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
