from django import forms
from .models import Entrepot, Adresse

class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['libelle', 'rue', 'complement', 'ville', 'etat', 'cp', 'pays']
        widgets = {
            'libelle':     forms.TextInput(attrs={'class': 'form-control'}),
            'rue':         forms.TextInput(attrs={'class': 'form-control'}),
            'complement':  forms.TextInput(attrs={'class': 'form-control'}),
            'ville':       forms.TextInput(attrs={'class': 'form-control'}),
            'etat':        forms.TextInput(attrs={'class': 'form-control'}),
            'cp':          forms.TextInput(attrs={'class': 'form-control'}),
            'pays':        forms.TextInput(attrs={'class': 'form-control'}),
        }
class EntrepotForm(forms.ModelForm):
    class Meta:
        model = Entrepot
        fields = ['nom', 'entreprise']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'entreprise': forms.Select(attrs={'class': 'form-control'}),
        }