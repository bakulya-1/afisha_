from rest_framework import serializers
from django.db.models import Avg
from rest_framework.serializers import raise_errors_on_nested_writes

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField(source='movies.count', read_only=True)
    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']


    def get_reviews(self, obj):
        reviews = Review.objects.filter(movie=obj)
        return ReviewSerializer(reviews, many=tuple).data

    def get_rating(self, obj):
        reviews = Review.objects.filter(movie=obj)
        if reviews.exists():
            average_rating = reviews.aggregate(models.Avg('stars'))['stars__avg']
            return round(average_rating, 2)
        return None


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']





