from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Superhero
from .forms import NewUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')

class SignUpView(CreateView):
    form_class = NewUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
class LogOutView(HttpRequest):
    def logout(request):
        return render(request, 'registration/logout.html')

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'heros/superhero_list.html'
    context_object_name = 'superheroes'

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'heros/superhero_detail.html'

class SuperheroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'heros/superhero_form.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    success_url = reverse_lazy('superhero_list')
    extra_context = {'title': 'Add New Superhero'}
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SuperheroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'heros/superhero_form.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    success_url = reverse_lazy('superhero_list')
    extra_context = {'title': 'Edit Superhero'}
    
    def get_queryset(self):
        return Superhero.objects.filter(author=self.request.user)

class SuperheroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'heros/superhero_confirm_delete.html'
    success_url = reverse_lazy('superhero_list')
    
    def get_queryset(self):
        return Superhero.objects.filter(author=self.request.user)