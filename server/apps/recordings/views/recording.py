from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.recordings.models.recording import Recording
from apps.recordings.serializers.recording import RecordingSerializer
from utils.google_speech import get_speech_data, get_dict
from utils.image_assembler import image_assembler
from django.core.files.base import ContentFile


# TODO: Classify record image + record text
class RecordView(APIView):

    def get(self, request):

        record_type = self.request.GET.get('type')

        # GET /record?type=text
        if record_type == 'text':
            return Response(status=status.HTTP_200_OK)

        # Default

        data = get_speech_data()
        print(data)

        dictionary = get_dict(data)
        print(dictionary)

        # Pass dictionary to classifier
        image = image_assembler.assemble(dictionary)
        print(image)

        text = ', '.join(data)
        print(text)

        # Save data to DB
        with open(image, 'rb') as f:
            data = f.read()
            recording = Recording(text=text)
            recording.image.save('output.png', ContentFile(data))


        serializer = RecordingSerializer(recording)
        return Response(serializer.data, status=status.HTTP_200_OK)

