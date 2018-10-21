from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.recordings.models.recording import Recording
from utils.google_speech import get_speech_data, get_dict
from utils.image_assembler import image_assembler


class RecordView(APIView):

    def get(self, request):
        data = get_speech_data()

        dictionary = get_dict(data)
        print(dictionary)

        # TODO: Pass dictionary to classifier
        image = image_assembler.assemble(dictionary)
        print(image)

        # TODO: Save data to DB
        # recording = Recording(text=text)
        # recording.save()

        return Response(data, status=status.HTTP_200_OK)

