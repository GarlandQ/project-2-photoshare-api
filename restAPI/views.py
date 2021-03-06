from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status, mixins, generics, permissions, viewsets
from users.models import Profile
from feed.models import Post, Comment
from restAPI.serializers import (
    ProfileSerializer,
    PostSerializer,
    CommentSerializer,
    PostUserSerializer,
    PostDetailSerializer,
)
from restAPI.permissions import IsOwnerOrReadOnly


# Essentially API homepage.
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "profiles": reverse("profile-list", request=request, format=format),
            "posts": reverse("post-list", request=request, format=format),
        }
    )


# List all user profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# List a specific user profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


# List all user posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# List a specific user post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# List a specific post's comments
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs["pk"])

    def get_queryset(self):
        post = self.kwargs["pk"]
        return Comment.objects.filter(post=post)
