from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Sala, Reserva

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class SalaSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de la sala"
    )
    disponible = forms.BooleanField(required=False, label="Sólo salas disponibles")
    capacidad_minima = forms.IntegerField(required=False, label="Salas con capacidad mayor a:")
    tipo_de_cancha = forms.ChoiceField(choices=Sala.Tipo.choices)


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput, help_text='Introduzca la misma contraseña que antes, para su verificación.')

    error_messages = {
        'password_mismatch': "Las dos contraseñas no coinciden.",
        'password_too_short': "Esta contraseña es demasiado corta. Debe contener al menos %(min_length)d caracteres.",
        'password_common': "Esta contraseña es demasiado común.",
        'password_entirely_numeric': "Esta contraseña es enteramente numérica.",
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

from .models import Sala, Reserva
from .models import Sala, Reserva

class ReservaSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de la reserva"
    )
    disponible = forms.BooleanField(required=False, label="Sólo reservas disponibles")
    capacidad_minima = forms.IntegerField(required=False, label="Reservas con capacidad mayor a:")

    CATEGORIA_CHOICES = [
        ('BASQUET', 'Cancha de Basquet '),
        ('FUTBOL', 'Cancha de Futbol'),
        ('TENIS', 'Cancha de Tenis '),
        ('SQUASH', 'Cancha de Squash'),
    ]
    
    categoria_de_reserva = forms.ChoiceField(choices=CATEGORIA_CHOICES, label="Categoría de reserva")


from django import forms
from .models import Reserva

class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre_de_usuario", "sala", "fecha", "hora_inicio", "hora_fin", "descripcion"]
