from django.urls import path
from .views import RegisterView, ConfirmEmailView, LoginView

urlpatterns = [
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/confirm/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('api/v1/login/', LoginView.as_view(), name='login'),
]
