from rest_framework import serializers
from django.db.models import Avg
from rest_framework.serializers import raise_errors_on_nested_writes
from django.db import models
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField(source='movies.count', read_only=True)
    class Meta:
        model = Director
        fields = ['id', 'name', 'movie_count']


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']


    def get_reviews(self, obj):
        reviews = obj.reviews.all()
        return ReviewSerializer(reviews, many=True).data

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
            return round(average_rating, 2)
        return None


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']





