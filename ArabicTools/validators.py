from ArabicTools.regex import ATTRIBUTES_REGEX, WORD
from django.core.validators import RegexValidator


class AttributesValidator(RegexValidator):
    regex = ATTRIBUTES_REGEX

class SpellingValidator(RegexValidator):
    regex = WORD