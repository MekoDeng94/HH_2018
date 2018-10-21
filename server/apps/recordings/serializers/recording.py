from rest_framework import serializers
from apps.recordings.models.recording import Recording


class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = '__all__'