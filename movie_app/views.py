from django.shortcuts import render
from rest_framework import generics, viewsets, status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, ConfirmUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "User registered successfully, please check your email for confirmation."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmUserView(generics.GenericAPIView):
    serializer_class = ConfirmUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = ConfirmUserSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "User confirmed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass



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


class MovieWithReviewsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MovieWithReviewsView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieWithReviewsPagination


