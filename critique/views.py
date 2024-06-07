from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ReviewViewset(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    