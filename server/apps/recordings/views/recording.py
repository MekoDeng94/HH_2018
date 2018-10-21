from django.conf import settings
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
        print(data)

        dictionary = get_dict(data)
        print(dictionary)

        # Pass dictionary to classifier
        save_path = settings.MEDIA_ROOT
        print(save_path)
        image = image_assembler.assemble(dictionary, save_path=save_path)
        print(image)

        text = ', '.join(data)
        print(text)

        # Save data to DB
        recording = Recording(text=text, image=image)
        recording.save()

        # TODO: Delete image

        return Response(data, status=status.HTTP_200_OK)

