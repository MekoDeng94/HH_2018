from django.contrib import admin
from apps.widgets.models.widget import Widget


class WidgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'text', 'image', 'height', 'width', 'top_position', 'left_position')


admin.site.register(Widget, WidgetAdmin)
