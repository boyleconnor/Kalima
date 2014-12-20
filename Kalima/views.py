from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


class DefaultView(RedirectView):
    url = reverse_lazy('dictionary:home')
    permanent = False