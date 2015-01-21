from copy import copy
from ArabicTools.constants import TASHKEEL, DIACRITICS, SHADDA, DEFAULT_ROOT


def form_to_template(form, root=DEFAULT_ROOT):
    template = ''
    counter = 0
    for letter in form:
        if letter == form[counter]:
            template += 'x'
        else:
            template += letter
    return template


def template_to_form(template, root=DEFAULT_ROOT):
    form = ''
    counter = 0
    for letter in template:
        if letter == 'x':
            form += root[counter]
            counter += 1
        else:
            form += letter
    return form


def extracter(word, form):
    if len(word) == len(form):
        iterations = len(word)
    word_copy = copy(word)
    for i in range(len(word)):
        pass


def apply(root_spelling, template):
    result = ''
    counter = 0
    for letter in template:
        if letter == 'x':
            result += root_spelling[counter]
            counter += 1
        else:
            result += letter
    return result


def spelling_to_template(word, root=('ف', 'ع', 'ل')):
    word = str(word)
    if ' ' in word or type(word) != str:
        raise ValueError()
    for i, j in enumerate(root):
        word.replace(j, ('\\%s' % i))
    return word


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