from .serializers import RegistrationSerializer,SetPasswordSerializer,GetUserDataSerializer,LoginUserSerializer, VerifyOTPSerializer,ResetPasswordSerializer,ResetPasswordConfirmView,UpdateProfileSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.emails import phone_or_mail
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import ScopedRateThrottle


usr = get_user_model()

class UpdateProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateProfileSerializer
    queryset = usr.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
    def get(self, request, *args, **kwargs):
        email = self.request.user.email
        image = self.request.user.image.url
        first_name = self.request.user.first_name 
        last_name = self.request.user.last_name 
        gender = self.request.user.gender
        birth_date = self.request.user.birth_date
        return Response({"email":email, "first_name":first_name, "last_name":last_name, "gender":gender, "birth_date":birth_date,'image':image,'success':True},status=status.HTTP_200_OK)
    def update(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
        email = self.request.user.email
        image = self.request.user.image.url
        first_name = self.request.user.first_name 
        last_name = self.request.user.last_name 
        gender = self.request.user.gender
        birth_date = self.request.user.birth_date
        return Response({"email":email, "first_name":first_name, "last_name":last_name, "gender":gender, "birth_date":birth_date,'image':image,'success':True},status=status.HTTP_200_OK)





class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            return Response({"Message":'Incorrect authentication details','success':False},status=status.HTTP_400_BAD_REQUEST)
        refresh = str(RefreshToken.for_user(user))
        access = str(AccessToken.for_user(user))
        return Response({"Message":'Authentication method is correct','access':access,'refresh':refresh,'success':True},status=status.HTTP_200_OK)


#class MyTokenObtainPairView(TokenObtainPairView):
#    serializer_class = MyTokenObtainPairSerializer
#    throttle_scope = 'login'
#    def post(self, request, *args, **kwargs):
#        response = super().post(request, *args, **kwargs)
#        if 'Unauthorized' in str(response.data):
#            return Response({"Message":'Incorrect cridentials','success':False},status = status.HTTP_400_BAD_REQUEST)
#        emial = self.request.data.get('email')
#        userstatus = User.objects.filter(email=emial)[0].status
#        if userstatus =='active':
#            return Response({"refresh":response.data['refresh'],"access":response.data['access'],'success':True},status = status.HTTP_200_OK)
#        return Response({"Message":'You should register your ','success':False},status = status.HTTP_400_BAD_REQUEST)


    #def post(self, request, *args, **kwargs):
    #    response = super().post(request, *args, **kwargs)   
    #    #userstatus = User.objects.filter(user_name=request.POST.get('user_name'))
    #    
    #    
    #    #print(userstatus)
    #    #print(request.POST.get('user_name'))
    #    return Response(,status=status.HTTP_200_OK)

# class LoginTokenGenerationAPIView(APIView):
    
#     def post(self, request, *args, **kwargs):
#         serializer = LoginTokenGenerationSerializer(data=request.data)
#         data = {}

#         if serializer.is_valid(raise_exception=True):
            
#             email = serializer.data['email']
#             password = serializer.data['password']
#             user_obj = User.objects.get(email=email)
            

#             try:
#                 if user_obj is not None:
#                     access_token = AccessToken.for_user(user=user_obj)
#                     refresh_token = RefreshToken.for_user(user=user_obj)
#                     data['refresh'] = str(access_token)
#                     data['access'] = str(refresh_token)

#             except Exception as e:
#                 return Response({'message':'username or password is incorrect'})
            
#         return Response(data, status.HTTP_200_OK)



class RegistrationAPIView(generics.GenericAPIView):
    '''Registers user'''
    serializer_class = RegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #data = {}
        user_status = ''
        email = request.data['email']

        try:
            user_status = User.objects.filter(email=email)[0].status
        except:
            pass
        
        message = {}
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            data = serializer.data['email']
            user_obj = User.objects.get(email=data)
            user_obj.status = 'inactive'
            user_obj.save()
            user_status = User.objects.filter(email=email)[0].status
            issended = phone_or_mail(serializer.data['email'])
            if issended is False:
                return Response({"Message":'invalid phone or email','success':False},status=status.HTTP_400_BAD_REQUEST)
            return Response({"Message":'Registration Successful. Otp sended to your mail please verify it and login','success':True},status=status.HTTP_200_OK)

        elif user_status=='active':
            return Response({"Message":'Status active please login','success':False},status=status.HTTP_404_NOT_FOUND)
        else:
            phone_or_mail(serializer.data['email'])
            return Response({"Message":'User exist but not active, Otp is sended','success':True},status=status.HTTP_200_OK)
    
    
class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user_status = ''
        email = request.data['email']
        try:
            user_status = User.objects.filter(email=email)[0].status
        except:
            pass
        if serializer.is_valid(raise_exception=True):
            if user_status=='active':
                issended = phone_or_mail(serializer.data['email'])
                if issended is False:
                    return Response({"Message":'invalid phone or email','success':False},status=status.HTTP_400_BAD_REQUEST)
                return Response({"Message":'Password set succesful','success':True},status=status.HTTP_200_OK)
            else:
                return Response({"Message":'Activate your account by registering','success':False},status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmView
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            otp = serializer.data['otp']
            try:
                user_obj = User.objects.get(email=email)
                data = {}
                if user_obj.otp == otp:
                    user_obj.status = 'active'
                    user_obj.save()
                    
                    refresh = RefreshToken.for_user(user=user_obj)
                    data['refresh'] = str(refresh)
                    data['access'] = str(refresh.access_token)
                    return Response({"refresh":data['refresh'],"access":data['access'],'success':True},status=status.HTTP_200_OK)
                return Response({"Message":'Otp doesnot match','success':False},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"Message":'Bad request','success':False},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":'Incorrect Auth methods','success':False},status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPAPIView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer
    def post(self, request, *args, **kwargs):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            otp = serializer.data['otp']
            try:
                user_obj = User.objects.get(email=email)
                data = {}
                if user_obj.otp == otp:
                    user_obj.status = 'active'
                    user_obj.save()
                    refresh = RefreshToken.for_user(user=user_obj)
                    data['refresh'] = str(refresh)
                    data['access'] = str(refresh.access_token)
                    return Response({"refresh":data['refresh'],"access":data['access'],'success':True},status=status.HTTP_200_OK)
                return Response({"Message":'Otp doesnot match','success':False},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"Message":'Bad request','success':False},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":'Incorrect Auth methods','success':False},status=status.HTTP_400_BAD_REQUEST)

class SetPasswordView(generics.GenericAPIView):
    serializer_class = SetPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            password1 = request.data['password']
            password2 =request.data['password2']
            if password1!= password2:
                return Response({'message':'passwords dont match',"success":False},status.HTTP_400_BAD_REQUEST)
            user = request.user
            user.set_password(password1)
            user.save()
        return Response({"Message":'Password set succesful','success':True},status=status.HTTP_200_OK)


class GetUserDataView(generics.ListAPIView):
    serializer_class = GetUserDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        serializer = GetUserDataSerializer(request.user)
        return Response({"userdata":serializer.data,'success':True},status=status.HTTP_200_OK)





class LogoutBlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"Message":'Password set succesful','success':False},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            
            return Response({"Message":'Password set succesful','success':False},status=status.HTTP_404_NOT_FOUND)

