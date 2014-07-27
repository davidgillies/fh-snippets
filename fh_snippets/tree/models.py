from django.db import models
from tags.models import Tag

# Create your models here.

class Tree(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    birth_date = models.CharField(max_length=10, blank=True)
    death_date = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    def __str__(self):
        return "%s %s" % (self.first_name, self.surname)

    class Meta:
        ordering = ('surname','birth_date',)

class Family(models.Model):
    husband = models.ForeignKey(Tree, related_name='hubbie')
    wife = models.ForeignKey(Tree, related_name='wiffy')
    marriage_date = models.CharField(max_length=20)
    marriage_place = models.CharField(max_length=50)
    children = models.ManyToManyField(Tree, related_name='kids')
    
    def __str__(self):
        return "%s, %s" % (self.husband.surname, self.wife.surname)
    
    
