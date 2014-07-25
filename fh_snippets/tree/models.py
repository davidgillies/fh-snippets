from django.db import models
from tags.models import Tag

# Create your models here.

class Tree(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    birth_date = models.CharField(max_length=10, blank=True)
    death_date = models.CharField(max_length=10, blank=True)
    marriages = models.ManyToManyField('self', blank=True, null=True)
    #parents = models.ForeignKey('self', blank=True, null=True)
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.surname)

    class Meta:
        ordering = ('surname','birth_date',)
