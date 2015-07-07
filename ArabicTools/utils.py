from ArabicTools.constants import DIACRITICS, DEFAULT_ROOT_SPELLING, ALLOWED_INFLECTION_ATTRIBUTES, POS_CHOICES, \
    ALLOWED_INFLECTION_ATTRIBUTE_VALUES
import re
from django.core.exceptions import ValidationError


def apply(origin_form, word, result_form):
    try:
        return re.match(origin_form, word).expand(result_form)
    except AttributeError:
        raise ValueError('word did not match origin_form')


def transcribe(spelling, code):
    output = ''
    for letter in spelling:
        if letter in code:
            new_letter = code[letter]
        else:
            new_letter = ' '
        if new_letter == '-' and len(output) > 0:
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


def attributes_to_dict(attributes):
    '''Converts a string containing attributes to a Python dictionary without performing any validation
    '''
    lines = attributes.split('\n')
    dict_out = {}
    for line in lines:
        attribute, value = line.split(':')
        dict_out[attribute] = value
    return dict_out


def dict_to_attributes(dict_in):
    ''' Converts a Python dictionary to a string containing attributes
    '''
    attributes = []
    for attribute, value in dict_in:
        attributes += [attribute + ':' + value + '\n']
    attributes = attributes.join('\n')
    return attributes


def validate_inflection_or_stem_attributes(part_of_speech, attributes):
    if part_of_speech not in dict(POS_CHOICES):
        raise ValidationError('part_of_speech not allowed part of speech')
    if part_of_speech not in ALLOWED_INFLECTION_ATTRIBUTES:
        raise ValidationError('part_of_speech does not have inflection attributes')
    attribute_dict = attributes_to_dict(attributes)
    for attribute in attribute_dict:
        if attribute not in ALLOWED_INFLECTION_ATTRIBUTE_VALUES:
            raise ValidationError('"%s" is not an allowed attribute' % attribute)
        if attribute not in ALLOWED_INFLECTION_ATTRIBUTES[part_of_speech]:
            raise ValidationError('"%s" is not an allowed attribute for part of speech "%s"' % (attribute, part_of_speech))
    return attribute_dict


def validate_inflection_attributes(part_of_speech, attributes):
    attribute_dict = validate_inflection_or_stem_attributes(part_of_speech, attributes)
    for attribute in attribute_dict:
        if attribute_dict[attribute] not in ALLOWED_INFLECTION_ATTRIBUTE_VALUES[attribute]:
            raise ValidationError('"%s" is not a valid value for attribute "%s"' % (attribute_dict[attribute], attribute))


def validate_stem_attributes(part_of_speech, attributes):
    attribute_dict = validate_inflection_or_stem_attributes(part_of_speech, attributes)
    for attribute in attribute_dict:
        values = attribute_dict[attribute].split('/')
        for value in values:
            if value not in ALLOWED_INFLECTION_ATTRIBUTE_VALUES[attribute]:
                raise ValidationError('"%s" is not a valid value for attribute "%s"' % (attribute_dict[attribute], attribute))
