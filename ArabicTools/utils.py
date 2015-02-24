from ArabicTools.constants import DIACRITICS, SHADDA, DEFAULT_ROOT
import re
from ArabicTools.regex import LETTER


def apply(origin_form, word, result_form):
    try:
        return re.match(origin_form, word).expand(result_form)
    except AttributeError:
        raise ValueError('word did not match origin_form')


def pattern_to_form(pattern):  # FIXME: This will break for patterns expecting more than three letters
    pattern = pattern.replace(LETTER, 'x')
    form = ''
    default_root = list(DEFAULT_ROOT)
    for letter in pattern:
        if letter == 'x':
            form += default_root.pop(0)
        else:
            form += letter
    return form


def transcribe(spelling, code):
    output = ''
    for letter in spelling:
        new_letter = code[letter]
        if new_letter == '-':
            output += output[-1]
        else:
            output += new_letter
    return output


def strip_diacritics(spelling, leave=[]):
    output = ''
    for letter in spelling:
        if (letter not in DIACRITICS) or (letter in leave):
            output += letter
    return output