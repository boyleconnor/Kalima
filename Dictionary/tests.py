from django.test import TestCase
from ArabicTools.constants import KAF, BAA, TAA, FAA, EIN, LAM, FATHA
from ArabicTools.regex import SOUND_LETTER
from ArabicTools.models import SpecialSet
from Dictionary.models import Word, Pattern


class PatternTestCase(TestCase):
    def test_pattern_apply(self):
        ORIGIN_FORM = ' '.join((FAA, EIN, LAM))
        RESULT_FORM = FAA+FATHA+TAA+FATHA+BAA+FATHA
        stem = Word.objects.create(
            spelling=' '.join((KAF, TAA, BAA)),
            pos='root',
            definition='do; make'
        )
        special_set = SpecialSet.objects.create(name='standard')
        for special_letter in (FAA, EIN, LAM):
            special_set.specials.create(key=special_letter, value=SOUND_LETTER)
        pattern = Pattern.objects.create(
            name='Form I (Fatha)',
            origin_pos='root',
            result_pos='verb',
            origin_form=ORIGIN_FORM,
            result_form=RESULT_FORM,
            special_set=special_set
        )
        result = pattern.apply(origin=stem)
        self.assertEqual(result.spelling, KAF+FATHA+TAA+FATHA+BAA+FATHA)
        self.assertEqual(result.pos, 'verb')
