"""
data model for blog post
"""
from django.db import models

class BlogPost(models.Model):
    '''A model is a class that represents table or collection in our DB,
    and where every attribute of the class is a field of the table or collection'''
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Author = models.CharField(max_length=50, null=True, blank=True)
    CreatedDate = models.DateField(auto_now=True)
    ReferenceLink = models.URLField(null=True, blank=True)

    class Meta: #pylint:disable=too-few-public-methods
        '''Model Meta is basically used to change the behavior of your model fields
        like changing order options,verbose_name and lot of other options.'''
        db_table = 'BlogPost'

    def __str__(self) -> str:
        return str(self.Title)
