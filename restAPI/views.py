from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from users.models import Profile
from restAPI.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class ProfileList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ProfileDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ProfileList(APIView):
#     def get(self, request, format=None):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class ProfileDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# def profile_list(request):
#     if request.method == "GET":
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def profile_detail(request, pk):
#     try:
#         profile = Profile.objects.get(pk=pk)
#     except Profile.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ProfileSerializer(profile)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(profile, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         profile.delete()
#         return HttpResponse(status=204)
