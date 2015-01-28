from ArabicTools.constants import DIACRITICS, SHADDA, DEFAULT_ROOT
import re
from ArabicTools.regex import LETTER


def apply(origin_form, word, result_form):
    return re.match(origin_form, word).expand(result_form)


def pattern_to_form(pattern):  # FIXME: This is fucking hideous
    pattern_ = list(pattern)
    default_root = list(DEFAULT_ROOT)
    for i in range(len(pattern_)):
        if (i+len(LETTER) <= len(pattern_)) and (''.join(pattern_[i:i+len(LETTER)]) == LETTER):
            pattern_[i] = default_root.pop(0)
            for j in range(i+1, i+len(LETTER)):
                pattern_.pop(i+1)
    pattern_ = ''.join(pattern_)
    return pattern_


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