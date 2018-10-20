from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.google_speech import get_speech_data, get_dict


class RecordView(APIView):

    def get(self, request):
        data = get_speech_data()

        # TODO: Save data to DB

        dictionary = get_dict(data)

        # TODO: Pass dictionary to classifier

        return Response(data, status=status.HTTP_200_OK)

