from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from Dictionary.models import Word


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['words'] = Word.objects.order_by('?')
        return context


class WordView(DetailView):
    template_name = 'word.html'
    model = Word
