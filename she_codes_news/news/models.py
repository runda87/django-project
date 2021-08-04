
from django.db import models
from django.contrib.auth import get_user_model
from django.forms.fields import URLField



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = 'stories'
    )

    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images',null=True)

#     story_image = models.URLField()

# class Image(models.Model):
#     title = models.CharField(max_length=200)


    def __str__(self):
        return self.title