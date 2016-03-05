from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from Dictionary.models import Word, Pattern
from Dictionary.forms import WordForm


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['words'] = Word.objects.order_by('?')
        return context


class WordView(DetailView):
    template_name = 'word.html'
    model = Word


class AddWordView(CreateView):
    template_name = 'add_word.html'
    model = Word
    form_class = WordForm


class PatternView(DetailView):
    template_name = 'pattern.html'
    model = Pattern
