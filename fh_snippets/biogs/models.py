from django.db import models
from tree.models import Tree, Family
from tags.models import Tag
from snippets.models import Snippet
# Create your models here.

class Biog(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    birth_year = models.CharField(max_length=4)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    tree_members = models.ManyToManyField(Tree, blank=True, null=True) 
    snippets = models.ManyToManyField(Snippet, blank=True, null=True)
    notes = models.TextField(blank=True)
    families = models.ManyToManyField(Family, blank=True, null=True)   
 
    def __str__(self):
        return "%s, %s" % (self.surname, self.first_name)

    class Meta:
        ordering = ('surname', 'first_name', 'birth_year',)

