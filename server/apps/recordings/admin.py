from django.contrib import admin
from apps.recordings.models.recording import Recording


class RecordingAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'image')


admin.site.register(Recording, RecordingAdmin)
