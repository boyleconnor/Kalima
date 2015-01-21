from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView, View


class DefaultView(RedirectView):
    url = reverse_lazy('dictionary:home')
    permanent = False