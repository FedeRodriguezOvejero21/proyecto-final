from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from Entrega_Final_FRO.models import Post, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Entrega_Final_FRO.forms import UsuarioForm
from Entrega_Final_FRO.models import Avatar,Post, Mensaje
from django.contrib.auth.models import User


#login_required
def index(request):
    posts = Post.objects.order_by("-publicado_el").all()
    return render(request,"Entrega_Final_FRO/index.html", {"posts": posts})

class PostDetalle(DetailView):
    model= Post

#aca protegi las vistas con el requiredmixin-LoginRequiredMixin
class PostListar(ListView):
    model= Post

class PostCrear(CreateView):
    model= Post
    success_url= reverse_lazy ("Entrega_Final_FRO-listar")
    fields= "__all__"

class PostBorrar(DeleteView):
    model= Post
    success_url= reverse_lazy ("Entrega_Final_FRO-listar")
    fields= "__all__"

class PostActualizar(UpdateView):
    model= Post
    success_url= reverse_lazy ("Entrega_Final_FRO-listar")
    fields= "__all__"

class UserSignUp(CreateView):
    form_class=UsuarioForm
    template_name= "registration/signup.html"
    success_url=reverse_lazy("Entrega_Final_FRO-listar")

class UserLogin(LoginView):
    next_page= reverse_lazy("Entrega_Final_FRO-listar")

class UserLogout(LogoutView):
    next_page= reverse_lazy("Entrega_Final_FRO-listar")

class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("Entrega_Final_FRO-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(DeleteView):
    model = Mensaje
    success_url = reverse_lazy("Entrega_Final_FRO-mensajes-listar")

class AvatarActualizar (UpdateView):
    model=Avatar
    fields=["imagen"]
    success_url= reverse_lazy("Entrega_Final_FRO-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ["first_name","last_name","email"]
    success_url= reverse_lazy("Entrega_Final_FRO-listar")

def about(request):
    return render(request, 'Entrega_Final_FRO-about.html')