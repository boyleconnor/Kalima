from ArabicTools.constants import TASHKEEL, DIACRITICS, SHADDA


def match_to_template():
    pass


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