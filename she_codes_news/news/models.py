from django.db import models
from django.contrib.auth import get_user_model
from django.forms.fields import URLField


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    story_image = models.URLField(default ='https://www.gaiaresources.com.au/wp-content/uploads/2020/02/SheCodes-cupcakes-narrow.jpg')
