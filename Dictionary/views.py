from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from Dictionary.models import Word


class Home(ListView):
    context_object_name = 'words'
    template_name = 'home.html'

    def get_queryset(self):
        return Word.objects.order_by('?')[:10]  # Get 10 random words


class WordCreate(CreateView):
    model = Word
    template_name = 'word/edit.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordUpdate(UpdateView):
    model = Word
    template_name = 'word/edit.html'


class WordDelete(DeleteView):
    model = Word