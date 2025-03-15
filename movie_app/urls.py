from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.DirectorListView.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view(), name='director-detail'),

    path('api/v1/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view(), name='movie-detail'),

    path('api/v1/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review-detail'),
]





