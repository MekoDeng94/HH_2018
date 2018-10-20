from django.urls import path
from apps.recordings.views.recording import RecordView


urlpatterns = [
    path('record', RecordView.as_view())
]
