from .serializers import MusicSerializer,MinusListSerializer,HistorySerializer,KaraokeListSerializer,SearchSerializer,CategorySerializer,CategoryNameListSerializer
from .models import Minus,Music,History,Category,CategoryName
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import generics 
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status 
from rest_framework.filters import SearchFilter,OrderingFilter
import json
# Create your views here.
class MusicView(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        data = History.objects.filter(user=self.request.user).order_by('-time_created')[:1]
        serializer = HistorySerializer(data, many=True)
        serializer.data[0] = serializer.data[0].pop('music')
        return Response({'minus':{'accompaniment':serializer.data[0]['accompaniment'],
        'vocals':serializer.data[0]['vocals'],
        'singer_name':serializer.data[0]['singer_name'],
        'song_name':serializer.data[0]['song_name'],
        'lyrics':serializer.data[0]['lyrics']},'success':True}, status=status.HTTP_200_OK)




class KaraokeView(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        data = History.objects.filter(user=self.request.user).order_by('-time_created')[:1]
        serializer = HistorySerializer(data, many=True)
        serializer.data[0] = serializer.data[0].pop('music')
        lyrics =serializer.data[0]['lyrics']
        return Response({'minus':{
            'accompaniment':serializer.data[0]['accompaniment'],
            'vocals':serializer.data[0]['vocals'],
            'singer_name':serializer.data[0]['singer_name'],
            'song_name':serializer.data[0]['song_name'],
            'background':serializer.data[0]['background'],
            'music_img':serializer.data[0]['music_img'],
            'lyrics':lyrics
        },'success':True}, status=status.HTTP_200_OK)


class HistoryView(generics.ListAPIView):
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-time_created')[:10]
        

class MinusListApiView(generics.ListAPIView):
    queryset = Minus.objects.all()
    serializer_class = MinusListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'success': True, 'Music_data': response.data,}
        return response

class KaraokeListApiView(generics.ListAPIView):
    queryset = Minus.objects.all()
    serializer_class = KaraokeListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'success': True, 'Music_data': response.data,}
        return response



class SearchView(generics.ListAPIView):
    queryset = Minus.objects.all()
    serializer_class = SearchSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('singer_name','song_name')
    permission_classes = [IsAuthenticated]
    pagination_class = None
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data = {'success':True,'data':response.data}
        return response


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    #def get(self, request, *args, **kwargs):
    #    serializer = Category.objects.filter(genre=kwargs['id'])
    #    serializer = CategorySerializer(data=serializer,many=True)
    #    
    #    if serializer.is_valid():
    #        return Response({'success':True,'data':serializer.data})
    #    return Response({'success':False,"msg":serializer.data})
    def list(self, request, *args, **kwargs):
        queryset = Category.objects.filter(genre = kwargs['id'])
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response({'success':True,'music':serializer.data})


class CategoryNameView(generics.ListAPIView):
    queryset = CategoryName.objects.all()
    serializer_class = CategoryNameListSerializer
    #pagination_class = None
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs) 
        response.data = {"success":True,'category':response.data}
        return response