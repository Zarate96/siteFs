from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class Inicio(UserPassesTestMixin, TemplateView):
    template_name = 'core/home.html'

    def test_func(self):
        return True
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title'] = 'Inicio'
        return context