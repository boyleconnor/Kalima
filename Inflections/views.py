from Inflections.models import Inflection, Stem, Stemmer, Paradigm, Inflecter
from Inflections.serializers import InflectionSerializer, StemSerializer, StemmerSerializer, ParadigmSerializer, InflecterSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class InflectionList(ListCreateAPIView):
    queryset = Inflection.objects.all()
    serializer_class = InflectionSerializer
    filter_fields = ('stem__parent',)


class InflectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Inflection.objects.all()
    serializer_class = InflectionSerializer


class StemList(ListCreateAPIView):
    queryset = Stem.objects.all()
    serializer_class = StemSerializer


class StemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stem.objects.all()
    serializer_class = StemSerializer


class StemmerList(ListCreateAPIView):
    queryset = Stemmer.objects.all()
    serializer_class = StemmerSerializer


class StemmerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stemmer.objects.all()
    serializer_class = StemmerSerializer


class ParadigmList(ListCreateAPIView):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ParadigmDetail(RetrieveUpdateDestroyAPIView):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class InflecterList(ListCreateAPIView):
    queryset = Inflecter.objects.all()
    serializer_class = InflecterSerializer


class InflecterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Inflecter.objects.all()
    serializer_class = InflecterSerializer
