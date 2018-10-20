from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.recordings.models.recording import Recording
from utils.google_speech import get_speech_data, get_dict


class RecordView(APIView):

    def get(self, request):
        data = get_speech_data()

        # Merge texts
        text = ' '.join(text) if len(text) > 1 else text 

        dictionary = get_dict(data)

        # TODO: Pass dictionary to classifier

        # TODO: Save data to DB
        # recording = Recording(text=text)
        # recording.save()

        return Response(data, status=status.HTTP_200_OK)

