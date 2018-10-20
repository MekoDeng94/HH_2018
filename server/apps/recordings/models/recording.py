import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('images', 'recordings', filename)

class Recording(models.Model):
    text = models.TextField(max_length=255, null=True, blank=True)
    image = image = models.ImageField(upload_to=get_image_path, null=True, blank=True)

    def __str__(self):
        return self.text