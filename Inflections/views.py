from Inflections.models import Inflection
from Inflections.serializers import InflectionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class InflectionList(ListCreateAPIView):
    queryset = Inflection.objects.all()
    serializer_class = InflectionSerializer
