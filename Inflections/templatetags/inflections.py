from Dictionary.models.Inflections import Inflection
from django import template

register = template.Library()

@register.simple_tag
def get_inflection(word, **attributes):
    inflections = [inflection.spelling for inflection in word.inflection_set.filter(**attributes)]
    if len(inflections) == 1:
        return inflections[0]
    elif len(inflections) > 1:
        return ' / '.join(inflections)
    elif len(inflections) == 0:
        return '-'


@register.simple_tag
def get_inflecter(pattern, **attributes):
    inflecters = [inflecter.get_result_form() for inflecter in pattern.inflecter_set.filter(**attributes)]
    if len(inflecters) == 1:
        return inflecters[0]
    elif len(inflecters) > 1:
        return ' / '.join(inflecters)
    elif len(inflecters) == 0:
        return '-'