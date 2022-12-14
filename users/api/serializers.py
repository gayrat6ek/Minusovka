from users.models import User
from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken


class UpdateProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields = ['email','first_name','last_name','gender','image','birth_date']
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class GetUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','first_name','last_name','gender','image','birth_date']
    


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)


#class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#    @classmethod
#    
#    def get_token(cls, user):
#        token = super().get_token(user)
#        return token
#    


class RegistrationSerializer(serializers.ModelSerializer):
    #password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields =  ['email']
        #extra_kwargs = {
        #    'password': {'write_only': True}
        #}
    def save(self):
        #password = self.validated_data['password']
        #password2 = self.validated_data['password2']
#
        #if password != password2:
        #    raise serializers.ValidationError(
        #        {'error': 'passwords did not match'})
    #            User.objects.create(email=self.validated_data['email'],
        user = User(email=self.validated_data['email'],is_active=True)
        #user.set_password(self.validated_data['password'])
        user.save()
        return user


class ResetPasswordSerializer(serializers.Serializer):
    
    email = serializers.CharField()


class ResetPasswordConfirmView(serializers.Serializer):
    email = serializers.CharField()
    otp = serializers.CharField()



        
class SetPasswordSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True,required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True,required=True)
    class Meta:
        model = User
        fields =  ['password','password2']
    



                    
class VerifyOTPSerializer(serializers.Serializer):

    email = serializers.CharField()
    otp = serializers.CharField()

# class CustomTokenRefreshViewSerializer(TokenRefreshView):
#     def validate(self, attrs):
#         # The default result (access/refresh tokens)
#         data = super(CustomTokenRefreshViewSerializer, self).validate(attrs)
#         # Custom data you want to include
#         data.update({'user': self.user.username})
#         data.update({'id': self.user.id})
#         # and everything else you want to send in the response
#         return data

# class LoginTokenGenerationSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
    
    