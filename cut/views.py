from django.shortcuts import render
from .serializers import Cutserializer
from rest_framework import generics
from rest_framework import response 
from rest_framework import status
from rest_framework import permissions
# Create your views here.


class CutView(generics.GenericAPIView):
    serializer_class = Cutserializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = request.data['cutting_music']
        data = str(data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if data.endswith('mp3'):
                serializer.save()
                return response.Response({'success':True,'link':serializer.data['cutted_music']},status=status.HTTP_201_CREATED)

        return response.Response({"message":'This is not music'},status= status.HTTP_200_OK)