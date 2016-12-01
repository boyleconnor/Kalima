from django.test import TestCase
from ArabicTools.constants import FAA, EIN, LAM, FATHA, DAMMA, SUKUN, KAF, TAA, BAA, YAA
from ArabicTools.regex import SOUND_LETTER
from ArabicTools.models import Special, SpecialSet
from Dictionary.models import Word
from Inflections.models import Stemmer, Stem, Inflecter


class StemmerTestCase(TestCase):
    def test_stemmer_apply(self):
        special_set = SpecialSet.objects.create(name='Sound Triliteral')
        for special_letter in (FAA, EIN, LAM):
            special_set.specials.create(key=special_letter, value=SOUND_LETTER)
        word = Word.objects.create(spelling=KAF + FATHA + TAA + FATHA + BAA + FATHA)

        origin_form = FAA + FATHA + EIN + FATHA + LAM + FATHA
        result_form = FATHA + FAA + SUKUN + EIN + DAMMA + LAM
        stemmer = Stemmer.objects.create(
            attributes='tense:present\n'+'mood:indicative',
            origin_form=origin_form,
            result_form=result_form,
            special_set=special_set
        )
        result = stemmer.apply(origin=word)
        self.assertEqual(result.spelling, FATHA+KAF+SUKUN+TAA+DAMMA+BAA)


class InflecterTestCase(TestCase):
    def test_inflecter_apply(self):
        special_set = SpecialSet.objects.create(name='Sound Triliteral')
        for special_letter in (FAA, EIN, LAM):
            special_set.specials.create(key=special_letter, value=SOUND_LETTER)
        word = Word.objects.create(spelling=KAF + FATHA + TAA + FATHA + BAA + FATHA) # kataba

        stem = Stem.objects.create(spelling=FATHA + KAF + SUKUN + TAA + DAMMA + BAA, parent=word)
        inflecter = Inflecter.objects.create(prefix=YAA, suffix=DAMMA)
        result = inflecter.apply(stem=stem)
        self.assertEqual(result.spelling, YAA+FATHA+KAF+SUKUN+TAA+DAMMA+BAA+DAMMA)
