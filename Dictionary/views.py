from Dictionary.forms import WordSearchForm, WordForm, DeriverForm
from Utils.mixins import ModelPermRequiredMixin, ObjPermRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from Dictionary.models import Word, Deriver
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


class WordCreate(ModelPermRequiredMixin, CreateView):
    model = Word
    permission_required = 'dictionary.add_word'
    form_class = WordForm
    template_name = 'word/edit.html'


class WordDetail(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordUpdate(ObjPermRequiredMixin, UpdateView):
    permission_required = 'dictionary.change_word'
    model = Word
    form_class = WordForm
    template_name = 'word/edit.html'


class WordDelete(ObjPermRequiredMixin, DeleteView):
    permission_required = 'dictionary.delete_word'
    model = Word


class DeriverCreate(ModelPermRequiredMixin, CreateView):
    permission_required = 'dictionary.add_deriver'
    model = Deriver
    form_class = DeriverForm
    template_name = 'deriver/edit.html'


class DeriverDetail(DetailView):
    model = Deriver
    template_name = 'deriver/detail.html'


class DeriverUpdate(ObjPermRequiredMixin, UpdateView):
    permission_required = 'dictionary.change_deriver'
    model = Deriver
    form_class = DeriverForm
    template_name = 'deriver/edit.html'