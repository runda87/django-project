from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountViews(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'user/profile.html'
    context_object_name = 'user'