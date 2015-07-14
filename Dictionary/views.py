from Dictionary.models import Word, Pattern
from Dictionary.serializers import WordSerializer, PatternSerializer, ApplySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.views.generic import DetailView, ListView


class WordList(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(RetrieveUpdateDestroyAPIView):
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

class PatternList(ListCreateAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer


class PatternApply(CreateAPIView):
    serializer_class = ApplySerializer
