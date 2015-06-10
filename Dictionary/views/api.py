from Dictionary.models import Word
from Dictionary.serializers import WordSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class WordList(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer