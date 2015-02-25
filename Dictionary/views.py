from Dictionary.forms import WordSearchForm, WordForm, DeriverForm, DeriverApplyForm
from Utils.mixins import ModelPermRequiredMixin, ObjPermRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormView
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
    template_name = 'word/delete.html'
    model = Word
    success_url = reverse_lazy('dictionary:home')


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


class DeriverDelete(ObjPermRequiredMixin, DeleteView):
    permission_required = 'dictionary.delete_deriver'
    model = Deriver
    template_name = 'deriver/delete.html'


class DeriverApply(ModelPermRequiredMixin, FormView):
    form_class = DeriverApplyForm
    template_name = 'deriver/apply.html'

    def dispatch(self, request, *args, **kwargs):
        self.deriver = get_object_or_404(Deriver, id=kwargs.pop('pk'))
        return super(DeriverApply, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_update_url()

    def get_form(self, form_class):
        form = super(DeriverApply, self).get_form(form_class)
        form.initial['deriver'] = self.deriver
        form.fields['stem'].queryset = Word.objects.filter(pos=self.deriver.origin_pos)
        return form

    def get_context_data(self, **kwargs):
        context_data = super(DeriverApply, self).get_context_data(**kwargs)
        context_data['deriver'] = self.deriver
        return context_data

    def form_valid(self, form):
        self.object = form.apply(self.deriver)
        return super(DeriverApply, self).form_valid(form)