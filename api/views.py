from .serializers import dictSerializer
from base.models import Word
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class getAll(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = dictSerializer
    pagination_class = StandardResultsSetPagination

class getOneByID(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = dictSerializer
    lookup_field = 'id'


class getSearches(generics.ListAPIView):
    serializer_class = dictSerializer
    pagination_class = StandardResultsSetPagination
    lookup_url_kwarg = 'word'

    def get_queryset(self):
        word = self.kwargs[self.lookup_url_kwarg]
        _from = self.request.query_params.get('from')

        if int(_from) == 1:
            # return Word.objects.filter(mar__istartswith=word) __iexact
            return Word.objects.filter(mar__iexact=word)
        else:
            # return Word.objects.filter(eng__istartswith=word)
            return Word.objects.filter(eng__iexact=word)



    