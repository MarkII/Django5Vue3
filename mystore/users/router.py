from django.urls import path
from users.views import RegisterUserView, UserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
    TokenObtainPairView -> Para hacer login con token
    TokenFreshView -> Para refrescar el token
"""

urlpatterns = [
    path('auth/register', RegisterUserView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh',  TokenRefreshView.as_view()),
    path('auth/user_info', UserView.as_view()),
]