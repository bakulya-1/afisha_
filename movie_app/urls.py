from django.urls import path
from pkg_resources.extern import names

from . import views

urlpatterns = [
    # Список режиссеров
    path('api/v1/directors/', views.DirectorViewSet.as_view(), name='director-list'),
    # Один режиссер
    path('api/v1/directors/<int:id>/', views.DirectorViewSet.as_view(), name='director-detail'),

    # Список фильмов
    path('api/v1/movies/', views.MovieViewSet.as_view(), name='movie-list'),
    # Один фильм
    path('api/v1/movies/<int:id>/', views.MovieViewSet.as_view(), name='movie-detail'),

    # Список отзывов
    path('api/v1/reviews/', views.ReviewViewSet.as_view(), name='review-list'),
    # Один отзыв
    path('api/v1/reviews/<int:id>/', views.ReviewViewSet.as_view(), name='review-detail'),

    # Список с рейтингом
    path('api/v1/movies/reviews/', views.MovieWithReviewsView.as_view(), name='movie-with-reviews'),
]





