from django.db import models
from tags.models import Tag


class Snippet(models.Model):
    BOOK = 'BK'
    MAP = 'MP'
    IMAGE = 'IMG'
    SOURCE_TYPES = (
        (BOOK, 'Book'),
        (MAP, 'Map'),
        (IMAGE, 'Image'),
    )

    snippet = models.TextField()
    source_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    source_type = models.CharField(
        max_length=10, choices=SOURCE_TYPES, default=BOOK)
    notes = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ('author',)
