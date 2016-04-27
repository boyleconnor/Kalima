from django.test import TestCase
from ArabicTools.utils import gen_origin_pattern, gen_result_pattern, apply
from ArabicTools.constants import *
from ArabicTools.regex import SOUND_LETTER

SPECIALS = {
    'X': '[a-zA-Z]+',
    'Y': '[a-z]+',
}
ORIGIN_FORM = "XYY"
RESULT_FORM = "XYYing"
WORD = "Boo"



class ApplyTestCase(TestCase):
    def test_gen_origin_pattern(self):
        origin_pattern = gen_origin_pattern(origin_form=ORIGIN_FORM, specials=SPECIALS)
        self.assertEqual(origin_pattern, "(?P<X>[a-zA-Z]+)(?P<Y>[a-z]+)(?P=Y)")

    def test_gen_result_pattern(self):
        result_pattern = gen_result_pattern(result_form=RESULT_FORM, specials=SPECIALS)
        self.assertEqual(result_pattern, "{X}{Y}{Y}ing")

    def test_apply(self):
        word = apply(origin_form=ORIGIN_FORM, specials=SPECIALS, word=WORD, result_form=RESULT_FORM)
        self.assertEqual(word, "Booing")
