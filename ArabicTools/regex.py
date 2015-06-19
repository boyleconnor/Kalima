from ArabicTools.constants import ABJAD, SOUND_LETTERS

LETTER = ('([%s])' % ABJAD)

SOUND_LETTER = '([%s])' % SOUND_LETTERS

SOUND_TRILITERAL = ' '.join(((SOUND_LETTER,) * 3))

WORD = ('([%s]+)')

ATTRIBUTES_REGEX = '^((.+):(.+))?(\n(.+):(.+))*$'