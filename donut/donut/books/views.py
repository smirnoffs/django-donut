from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT
from rest_framework.viewsets import GenericViewSet
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

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
        """Marks the book as published"""
        book = self.queryset.get(pk=pk)
        if book.published is True:
            return Response(status=HTTP_409_CONFLICT)
        return Response(status=HTTP_201_CREATED)


books_schema_view = get_schema_view(
    title="Books API",
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
)
