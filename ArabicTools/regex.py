from ArabicTools.constants import ABJAD, SOUND_LETTERS, ARABIC_CHARACTERS

LETTER = ('([%s])' % ABJAD)

SOUND_LETTER = '([%s])' % SOUND_LETTERS

SOUND_TRILITERAL = ' '.join(((SOUND_LETTER,) * 3))

WORD = '[%s]+' % ARABIC_CHARACTERS

ATTRIBUTES_REGEX = '^((.+):(.+))?(\n(.+):(.+))*$'