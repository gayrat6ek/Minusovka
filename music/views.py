from .serializers import MusicSerializer,MinusSerializer,HistorySerializer
from .models import Minus,Music,History
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status 
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
        return Response({'minus':{'accompaniment':serializer.data[0],
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
        return Response({'minus':{
            'accompaniment':serializer.data[0]['accompaniment'],
            'vocals':serializer.data[0]['vocals'],
            'background':serializer.data[0]['background'],
            'music_img':serializer.data[0]['music_img'],
            'lyrics':serializer.data[0]['lyrics'],
        },'success':True}, status=status.HTTP_200_OK)

class MinusView(generics.ListAPIView):
    queryset = Minus.objects.all()
    serializer_class = MinusSerializer

class HistoryView(generics.ListAPIView):
    serializer_class = HistorySerializer
    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-time_created')[:10]


        
        
