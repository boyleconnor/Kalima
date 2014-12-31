from Dictionary.forms import WordSearchForm


def search(request):
    return {'search_form': WordSearchForm}