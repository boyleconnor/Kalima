from ArabicTools.constants import *


def mass_inflect(word, filters=[]):
    if not word.pattern:
        raise RuntimeError("'word' must have 'pattern' in order to use mass_inflect")
    inflecters = word.pattern.inflecter_set.all()
    used_inflections = [inflection.pattern for inflection in word.inflection_set.all()]
    inflecters = inflecters.exclude(id__in=[used_inflection.id for used_inflection in used_inflections])
    for filter in filters:
        inflecters = inflecters.filter(result_form__regex=filter)
    for inflecter in inflecters:
        inflecter.apply(word, save=True)


def noun_broken_plural(word, plural):
    for state, template in {'definite': ALIF+LAM+'%s%s'}:
        if True:
            for case in {'nominative': DAMMA, 'genitive': KASRA, 'accusative': FATHA}:
                word.inflection_set.create(case=case)


def adjective_broken_plural(word, plural):
    pass