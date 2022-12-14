from django.urls import path
from .views import RegistrationAPIView,SetPasswordView,LoginUserView,GetUserDataView, VerifyOTPAPIView, LogoutBlacklistTokenUpdateView,ResetPasswordConfirmView,ResetPasswordView,UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('verify/', VerifyOTPAPIView.as_view(), name='verify-otp'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutBlacklistTokenUpdateView.as_view(), name='logout'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('setpassword/',SetPasswordView.as_view(),name='setpassword'),
    path('resetpassword/',ResetPasswordView.as_view(),name='resetpassword'),
    path('resetpasswordconfirm/',ResetPasswordConfirmView.as_view(),name='resetpasswordconfirm'),
    path('login/',LoginUserView.as_view(),name='loginuser'),
    path('update/profile/',UpdateProfileView.as_view(),name='profile'),
    path('getuserinfo/',GetUserDataView.as_view(),name='data')
]
