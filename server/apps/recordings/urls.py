from django.urls import path
from apps.recordings.views.recording import RecordView, RecordTextView


urlpatterns = [
    path('record', RecordView.as_view()),
    path('record/text', RecordTextView.as_view())
]
