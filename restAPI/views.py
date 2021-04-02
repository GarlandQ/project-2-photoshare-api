from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status, mixins, generics, permissions
from users.models import Profile
from restAPI.serializers import ProfileSerializer
from restAPI.permissions import IsOwnerOrReadOnly


# List all user profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# List a specific user profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# Essentially API homepage.
# Adding more links as I go on when necessary...
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "profiles": reverse("profile-list", request=request, format=format),
        }
    )
