from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import BlogsLevelOne, BlogsLevelThree, BlogsMaxClearance
from .permissions import DynamicClearancePermission
from .serializers import BlogSerializer


class BlogsLevelOneViewSet(viewsets.ModelViewSet):
    queryset = BlogsLevelOne.objects.all()
    serializer_class = BlogSerializer
    permission_classes  = [DynamicClearancePermission]
    required_level = 1

class BlogsLevelThreeViewSet(viewsets.ModelViewSet):
    queryset = BlogsLevelThree.objects.all()
    serializer_class = BlogSerializer
    permission_classes  = [DynamicClearancePermission]
    required_level = 3


class BlogsMaxClearanceViewSet(viewsets.ModelViewSet):
    queryset = BlogsMaxClearance.objects.all()
    serializer_class = BlogSerializer
    permission_classes  = [DynamicClearancePermission]
    required_level = 4