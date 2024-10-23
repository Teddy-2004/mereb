from django.urls import path
from .views import RegisterView
from .views import CustomPasswordResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
