from Dictionary.models import Word, Pattern
from Dictionary.serializers import WordSerializer, PatternSerializer, ApplySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


class WordList(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class PatternList(ListCreateAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternApply(CreateAPIView):
    serializer_class = ApplySerializer