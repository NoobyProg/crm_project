from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy

class HomeView(LoginView):
    template_name = 'common/home.html'

class DashboardView(TemplateView):
    template_name = 'common/dashboard.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'