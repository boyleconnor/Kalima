from django.contrib.auth.decorators import permission_required as perm_required_decorator
from django.utils.decorators import method_decorator


class ModelPermRequiredMixin:
    permission_required = ''

    @method_decorator(perm_required_decorator(permission_required))
    def dispatch(self, request):
        return super(ModelPermRequiredMixin, self).dispatch(request)