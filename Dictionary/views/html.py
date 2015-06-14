from Dictionary.forms import WordSearchForm, WordForm, PatternForm, PatternApplyForm
from Utils.mixins import ModelPermRequiredMixin, ObjPermRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormView
from Dictionary.models import Word, Pattern
from haystack.views import SearchView, search_view_factory


class Home(ListView):
    context_object_name = 'words'
    template_name = 'home.html'

    def get_queryset(self):
        return Word.objects.order_by('?')[:10]  # Get 10 random words


class WordSearch:
    @staticmethod
    def as_view():
        return search_view_factory(view_class=SearchView, form_class=WordSearchForm, template='search.html')


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
    template_name = 'word/delete.html'
    model = Word
    success_url = reverse_lazy('dictionary:home')


class PatternCreate(ModelPermRequiredMixin, CreateView):
    permission_required = 'dictionary.add_pattern'
    model = Pattern
    form_class = PatternForm
    template_name = 'pattern/edit.html'


class PatternDetail(DetailView):
    model = Pattern
    template_name = 'pattern/detail.html'


class PatternUpdate(ObjPermRequiredMixin, UpdateView):
    permission_required = 'dictionary.change_pattern'
    model = Pattern
    form_class = PatternForm
    template_name = 'pattern/edit.html'


class PatternDelete(ObjPermRequiredMixin, DeleteView):
    permission_required = 'dictionary.delete_pattern'
    model = Pattern
    template_name = 'pattern/delete.html'
    success_url = reverse_lazy('dictionary:home')


class PatternApply(ModelPermRequiredMixin, FormView):
    form_class = PatternApplyForm
    template_name = 'pattern/apply.html'

    def dispatch(self, request, *args, **kwargs):
        self.pattern = get_object_or_404(Pattern, id=kwargs.pop('pk'))
        return super(PatternApply, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_update_url()

    def get_form(self, form_class):
        form = super(PatternApply, self).get_form(form_class)
        form.initial['pattern'] = self.pattern
        form.fields['stem'].queryset = Word.objects.filter(pos=self.pattern.origin_pos)
        return form

    def get_context_data(self, **kwargs):
        context_data = super(PatternApply, self).get_context_data(**kwargs)
        context_data['pattern'] = self.pattern
        return context_data

    def form_valid(self, form):
        self.object = form.apply(self.pattern)
        return super(PatternApply, self).form_valid(form)