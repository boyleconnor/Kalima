from django.contrib.auth.decorators import permission_required as perm_required_decorator
from django.utils.decorators import method_decorator
from guardian.mixins import PermissionRequiredMixin


class ModelPermRequiredMixin:
    permission_required = ''

    @method_decorator(perm_required_decorator(permission_required, raise_exception=True))
    def dispatch(self, request):
        return super(ModelPermRequiredMixin, self).dispatch(request)


class ObjPermRequiredMixin(PermissionRequiredMixin):
    raise_exception = True