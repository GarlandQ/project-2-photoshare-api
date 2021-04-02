from rest_framework import serializers
from users.models import Profile
from feed.models import Post, Comment
from django.contrib.auth.models import User


# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(source="user.username", read_only=True)

#     class Meta:
#         model = Profile
#         fields = ["id", "user", "image", "bio"]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # Link to user profile page
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "image", "bio", "url"]
