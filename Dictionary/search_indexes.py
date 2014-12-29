from Dictionary.models import Word
from haystack.fields import CharField
from haystack.indexes import SearchIndex, Indexable


class WordIndex(SearchIndex, Indexable):
    spelling = CharField(model_attr='spelling')
    definition = CharField(model_attr='definition')
    text = CharField(document=True, use_template=True, template_name='word/search_text')

    def get_model(self):
        return Word