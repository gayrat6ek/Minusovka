from django.shortcuts import render
from .serializers import Cutserializer,MixMusicSerializer,VolumeMixSerializer
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

        return response.Response({"message":'This is not music','success':False},status= status.HTTP_400_BAD_REQUEST)


class MixMusicView(generics.GenericAPIView):
    serializer_class = MixMusicSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        first = request.data['first_music']
        second = request.data['second_music']
        first = str(first)
        second = str(second)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if first.endswith('mp3') and second.endswith('mp3'):
                serializer.save()
                return response.Response({'success':True,"link":serializer.data['mixed_music']},status=status.HTTP_200_OK)

        return response.Response({"message":'This is not music','success':False},status= status.HTTP_400_BAD_REQUEST)


class VolumeMixView(generics.GenericAPIView):
    serializer_class = VolumeMixSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        first = request.data['instrumental']
        second = request.data['vocals']
        first = str(first)
        second = str(second)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if first.endswith('mp3') and second.endswith('mp3'):
                serializer.save()
                return response.Response({'success': True, "link": serializer.data['joined_music']}, status=status.HTTP_200_OK)


        return response.Response({"message":'This is not music','success':False},status= status.HTTP_400_BAD_REQUEST)