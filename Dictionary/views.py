from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Dictionary.models import Word


class WordCreate(CreateView):
    model = Word


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordUpdate(UpdateView):
    model = Word


class WordDelete(DeleteView):
    model = Word