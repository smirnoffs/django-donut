from django.db import models


class Book(models.Model):
    class Meta:
        app_label = "books"

    author = models.CharField(max_length=300, null=False, blank=False)
    title = models.CharField(max_length=333, null=False, blank=False)
    published = models.BooleanField(default=False)
