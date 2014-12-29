from Dictionary.forms import WordSearchForm, WordForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from guardian.mixins import PermissionRequiredMixin
from Dictionary.models import Word
from haystack.views import SearchView, search_view_factory


class Home(ListView):
    context_object_name = 'words'
    template_name = 'home.html'

    def get_queryset(self):
        return Word.objects.order_by('?')[:10]  # Get 10 random words


class WordSearch:
    @staticmethod
    def as_view():
        return search_view_factory(view_class=SearchView, form_class=WordSearchForm, template='word/search.html')


class WordCreate(PermissionRequiredMixin, CreateView):
    accept_global_perms = True
    permission_required = 'dictionary.add_word'
    model = Word
    form_class = WordForm
    template_name = 'word/edit.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'dictionary.change_word'
    model = Word
    form_class = WordForm
    template_name = 'word/edit.html'


class WordDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'dictionary.delete_word'
    model = Word