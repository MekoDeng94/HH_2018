from django.db import models
from apps.widgets.models.widget import Widget


class Layout(models.Model):
    widgets = models.ManyToManyField(Widget)

    def __str__(self):
        return ', '.join(w.__str__() for w in self.widgets.all())
