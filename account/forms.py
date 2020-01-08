from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30,
                                 required=False)
    número_de_telefone = forms.CharField(label="Número de telefone",
                                   widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}))

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='Repitir Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))

    class Meta:
        model = User
        fields = ('first_name', 'número_de_telefone')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)


        user.save()

        return user
