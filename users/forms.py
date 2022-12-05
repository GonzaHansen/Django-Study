from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #Default es True es decir es obligatorio

    class Meta: #Configuracion del modelo usuario
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #En que orden se mostrara el form
        
