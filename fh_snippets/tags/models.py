from django.db import models


class Tag(models.Model):
    OCCUPATION = 'occ'
    LOCATION = 'loc'
    PERIOD = 'per'
    PERSON = 'ppe'
    SUBJECT = 'sub'
    TAG_TYPE_CHOICES = (
        (OCCUPATION, 'Occupation'),
        (LOCATION, 'location'),
        (PERIOD, 'Period'),
        (PERSON, 'Person'),
        (SUBJECT, 'Subject'),
    )

    tagname = models.CharField(max_length=200)
    description = models.TextField()
    tag_type = models.CharField(max_length=10, choices=TAG_TYPE_CHOICES)

    def __str__(self):
        return self.tagname

    class Meta:
        ordering = ('tag_type',)
