from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ConfirmEmail

urlpatterns = [
    path('', jwt_views.TokenObtainPairView.as_view()),
    path('refresh/', jwt_views.TokenRefreshView.as_view()),
    path('verify/', ConfirmEmail.as_view())
]
