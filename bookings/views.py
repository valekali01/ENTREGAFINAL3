from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SalaSearchForm
from .models import Reserva, Sala

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")


# -----------------------------------------------------------------------------
# CRUD: SALAS
# -----------------------------------------------------------------------------

# List

class SalaListView(LoginRequiredMixin, ListView):
    model = Sala
    template_name = "bookings/vbc/sala_list.html"
    context_object_name = "ADRIANDARGELOS"


class SalaDetailView(LoginRequiredMixin, DetailView):
    model = Sala
    template_name = "bookings/vbc/sala_detail.html"
    context_object_name = "GUSTAVOCERATI"


class SalaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = "bookings/vbc/sala_confirm_delete.html"
    success_url = reverse_lazy("sala-list")


class SalaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre", "disponible", "capacidad"]
    context_object_name = "sala"
    success_url = reverse_lazy("sala-list")


class SalaCreateView(LoginRequiredMixin, CreateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre","tipo", "disponible", "capacidad"]
    success_url = reverse_lazy("sala-list")



def sala_search_view(request):
    if request.method == "GET":
        form = SalaSearchForm()
        return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        form = SalaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_sala = form.cleaned_data["nombre"]
            descartar_no_disponibles = form.cleaned_data["disponible"]
            capacidad_minima = form.cleaned_data["capacidad_minima"]
            tipo_de_sala = form.cleaned_data["tipo_de_sala"]

            salas_encontradas = Sala.objects.filter(nombre__icontains=nombre_de_sala)

            if descartar_no_disponibles:
                salas_encontradas = salas_encontradas.filter( disponible=True)

            if capacidad_minima:
                salas_encontradas = salas_encontradas.filter(capacidad__gte=capacidad_minima)

            if tipo_de_sala:
                salas_encontradas = salas_encontradas.filter(tipo=tipo_de_sala)



            contexto_dict = {"ADRIANDARGELOS": salas_encontradas}
            return render(request, "bookings/vbc/sala_list.html", contexto_dict)
        else:
            return render(
                request, "bookings/form_search.html", context={"search_form": form}
            )


# -----------------------------------------------------------------------------
# login / logout
# -----------------------------------------------------------------------------

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "bookings/login.html", {"MICHAELSTIPE": form})


def user_logout_view(request):
    logout(request)
    return redirect("login")

# -----------------------------------------------------------------------------
# Editar usuario
# -----------------------------------------------------------------------------

from django.contrib.auth.models import User
from .forms import UserEditForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

# ------------------------------------------------------------------------
# Clase 25
# ------------------------------------------------------------------------

from .models import Avatar
from .forms import AvatarCreateForm


def avatar_view(request):
    if request.method == "GET":
        contexto = {"PABLOCALA": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"PABLOCALA": form}


    return render(request, "bookings/avatar_create.html", context=contexto)

from .forms import CustomUserCreationForm

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'bookings/create_user.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Reserva
from .forms import SalaForm, ReservaForm

def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'bookings/lista_reservas.html', {'reservas': reservas})

def reserva_detail(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'bookings/detalle_reserva.html', {'reserva': reserva})

def reserva_create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva-detail', pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, 'bookings/form_reserva.html', {'form': form})

def reserva_update(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva-detail', pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'bookings/form_reserva.html', {'form': form})

def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva-list')
    return render(request, 'bookings/confirm_delete_reserva.html', {'object': reserva})


