from rest_framework import serializers

from donut.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id', ]
