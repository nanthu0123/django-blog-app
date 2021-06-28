from django.db import models


class BlogPost(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Author = models.CharField(max_length=50, null=True, blank=True)
    CreatedDate = models.DateField(auto_now=True)
    ReferenceLink = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'BlogPost'

    def __str__(self) -> str:
        return self.Title
