from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ejemplo_dos.forms import UsuarioForm
from ejemplo_dos.models import Avatar,Post
from django.contrib.auth.models import User


#login_required
def index(request):
    posts = Post.objects.order_by("-publicado_el").all
    return render(request,"ejemplo_dos/index.html", {"posts": posts})

class PostDetalle(DetailView):
    model= Post

#aca protegi las vistas con el requiredmixin-LoginRequiredMixin
class PostListar(ListView):
    model= Post

class PostCrear(CreateView):
    model= Post
    success_url= reverse_lazy ("ejemplo-dos-listar")
    fields= "__all__"

class PostBorrar(DeleteView):
    model= Post
    success_url= reverse_lazy ("ejemplo-dos-listar")
    fields= "__all__"

class PostActualizar(UpdateView):
    model= Post
    success_url= reverse_lazy ("ejemplo-dos-listar")
    fields= "__all__"

class UserSignUp(CreateView):
    form_class=UsuarioForm
    template_name= "registration/signup.html"
    success_url=reverse_lazy("ejemplo-dos-listar")

#http://127.0.0.1:8000/ejemplo-dos/login/
class UserLogin(LoginView):
    next_page= reverse_lazy("ejemplo-dos-listar")

class UserLogout(LogoutView):
    next_page= reverse_lazy("ejemplo-dos-listar")

class AvatarActualizar (UpdateView):
    model=Avatar
    fields=["imagen"]
    succss_url= reverse_lazy("ejemplo-dos-listar")

class UserActualizar(UpdateView):
    model = User
    field = ["first_name","last_name","email"]
    succss_url= reverse_lazy("ejemplo-dos-listar")