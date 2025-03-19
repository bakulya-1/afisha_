from django.shortcuts import render
from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import NotFound



class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        director_id = kwargs.get('pk')
        try:
            director = Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise NotFound("Director not found.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        director_id = kwargs.get('pk')
        try:
            director = Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise NotFound("director not found")
        return super().destroy(request, *args, **kwargs)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    def update(self, request, *args, **kwargs):
        movie_id = kwargs.get('pk')
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise NotFound("Movie not found.")
        return super().update(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        movie_id = kwargs.get('pk')
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise NotFound("Movie not found.")
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def update(self, request, *args, **kwargs):
        review_id = kwargs.get('pk')
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise NotFound("Review not found.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        review_id = kwargs.get('pk')
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise NotFound("Review not found.")
        return super().destroy(request, *args, **kwargs)


class MovieWithReviewsView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


