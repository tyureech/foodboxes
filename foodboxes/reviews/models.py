from django.db import models
from django.conf import settings


class Reviews(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    text = models.TextField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField()
    status = models.CharField(max_length=7)

