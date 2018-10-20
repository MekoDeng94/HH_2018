import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('images', filename)

class Widget(models.Model):
    type = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    top_position = models.DecimalField(max_digits=4, decimal_places=2)
    left_position = models.DecimalField(max_digits=4, decimal_places=2)