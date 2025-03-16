from django.urls import path
from pkg_resources.extern import names

from . import views

urlpatterns = [
    # Список режиссеров
    path('api/v1/directors/', views.DirectorListView.as_view(), name='director-list'),
    # Один режиссер
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view(), name='director-detail'),

    # Список фильмов
    path('api/v1/movies/', views.MovieListView.as_view(), name='movie-list'),
    # Один фильм
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view(), name='movie-detail'),

    # Список отзывов
    path('api/v1/reviews/', views.ReviewListView.as_view(), name='review-list'),
    # Один отзыв
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review-detail'),

    # Список с рейтингом
    path('api/v1/moviews/reviews/', views.MovieWithReviewsView.as_view(), names='movie-with-reviews'),
]





