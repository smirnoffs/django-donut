import json

from django.test import Client
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_409_CONFLICT

from donut.books.models import Book

title = 'Peter Pan'
author = 'Sir James Matthew Barrie'

client = Client()


def test_create_book(db):
    response = client.post('/books/', {'title': title, 'author': author})
    assert response.status_code == HTTP_201_CREATED
    book = Book.objects.get()
    assert book.title == title
    assert book.author == author
    assert book.published is False


def test_get_book(db):
    book = Book.objects.create(title=title, author=author)
    response = client.get(f'/books/{book.id}/')
    assert response.status_code == HTTP_200_OK
    assert json.loads(response.content) == {'title': title, 'author': author, 'published': False}


def test_publish_book(db):
    book = Book.objects.create(title=title, author=author, published=False)
    response = client.post(f'/books/{book.id}/publish/')
    assert response.status_code == HTTP_201_CREATED
    book.refresh_from_db()
    book.published = True


def test_publish_book_cannot_republish_a_published_one(db):
    book = Book.objects.create(title=title, author=author, published=True)
    response = client.post(f'/books/{book.id}/publish/')
    assert response.status_code == HTTP_409_CONFLICT
