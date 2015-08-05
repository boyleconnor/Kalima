from Inflections.models import Inflection, Stem
from Inflections.serializers import InflectionSerializer, StemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class InflectionList(ListCreateAPIView):
    queryset = Inflection.objects.all()
    serializer_class = InflectionSerializer


class InflectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Inflection.objects.all()
    serializer_class = InflectionSerializer


class StemList(ListCreateAPIView):
    queryset = Stem.objects.all()
    serializer_class = StemSerializer


class StemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stem.objects.all()
    serializer_class = StemSerializer
