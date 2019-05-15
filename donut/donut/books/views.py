from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT
from rest_framework.viewsets import GenericViewSet

from donut.books.models import Book
from donut.books.serializers import BookSerializer


class BookViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    """
    Book API endpoint that allows to add, edit, delete, view books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=('POST',), url_path='publish', detail=True)
    def publish(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book.published is True:
            return Response(status=HTTP_409_CONFLICT)
        return Response(status=HTTP_201_CREATED)
