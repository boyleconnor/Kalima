from Dictionary.models import Word, Pattern
from Dictionary.serializers import WordSerializer, PatternSerializer, ApplySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.views.generic import DetailView, ListView


class WordListJSON(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetailJSON(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetailHTML(DetailView):
    model = Word
    template_name = 'word/detail.html'


class WordListHTML(ListView):
    model = Word
    template_name = 'word/list.html'

    def filter_queryset(self, queryset):
        if self.request.GET:
            return queryset.filter(**self.request.GET.dict())
        return queryset

    def get_queryset(self):
        queryset = super(WordListHTML, self).get_queryset()
        return self.filter_queryset(queryset)

class PatternListJSON(ListCreateAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternDetailJSON(RetrieveUpdateDestroyAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternApplyJSON(CreateAPIView):
    serializer_class = ApplySerializer
