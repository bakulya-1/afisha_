from django.urls import path
from pkg_resources.extern import names
from .views import RegisterView, ConfirmUserView, MyTokenObtainPairView, MyTokenRefreshView
from .views import DirectorViewSet, MovieViewSet, ReviewViewSet, MovieWithReviewsView
from . import views

urlpatterns = [
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/users/confirm/', ConfirmUserView.as_view(), name='confirm_user'),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),


    path('api/v1/directors/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director-list'),
    path('api/v1/directors/<int:id>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='director-detail'),



    path('api/v1/movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('api/v1/movies/<int:id>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie-detail'),


    path('api/v1/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),


    path('api/v1/movies/reviews/', MovieWithReviewsView.as_view(), name='movie-with-reviews'),
]






