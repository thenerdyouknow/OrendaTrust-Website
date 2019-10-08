from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255, default='')
    body = RichTextField()

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
