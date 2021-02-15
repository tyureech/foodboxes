from django.db import models


class Items(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)


