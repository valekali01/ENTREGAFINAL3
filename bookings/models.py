from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"Avatar for {self.user.username}"


class Sala(models.Model):
    class Tipo(models.TextChoices):
        AUDITORIO = 'BASQUET', 'Cancha de Basquet '
        SALA_DE_CONFERENCIAS = 'FUTBOL', 'Cancha de Futbol'
        AULA = 'TENIS', 'Cancha de Tenis '
        LABORATORIO = 'SQUASH', 'Cancha de Squash'

    nombre = models.CharField(max_length=40)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)  # Puedes definir un valor predeterminado si lo deseas
    tipo = models.CharField(
        max_length=7,
        choices=Tipo.choices,
        default=Tipo.AULA,
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Reserva(models.Model):
    nombre_de_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="reservas")
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.sala.nombre} - {self.fecha}"
    
class Reserva(models.Model):
    class Tipo(models.TextChoices):
        AUDITORIO = 'BASQUET', 'Cancha de Basquet '
        SALA_DE_CONFERENCIAS = 'FUTBOL', 'Cancha de Futbol'
        AULA = 'TENIS', 'Cancha de Tenis '
        LABORATORIO = 'SQUASH', 'Cancha de Squash'

    nombre = models.CharField(max_length=40)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    tipo = models.CharField(
        max_length=7,
        choices=Tipo.choices,
        default=Tipo.AULA,
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class Reserva(models.Model):
    class Tipo(models.TextChoices):
        AUDITORIO = 'BASQUET', 'Cancha de Basquet '
        SALA_DE_CONFERENCIAS = 'FUTBOL', 'Cancha de Futbol'
        AULA = 'TENIS', 'Cancha de Tenis '
        LABORATORIO = 'SQUASH', 'Cancha de Squash'

    nombre_de_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="reservas")
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    tipo_de_reserva = models.CharField(
        max_length=7,
        choices=Tipo.choices,
        default=Tipo.AULA,
    )

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.sala.nombre} - {self.fecha}"


# bookings/models.py

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# bookings/models.py

from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
