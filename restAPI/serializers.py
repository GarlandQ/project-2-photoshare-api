from rest_framework import serializers
from users.models import Profile
from feed.models import Post, Comment
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    # Link to user profile page
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )
    # user = serializers.CharField(source="user.username", read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["id", "user", "image", "bio", "url"]

    def get_user(self, obj):
        return obj.user.username


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )

    url = serializers.HyperlinkedIdentityField(view_name="post-detail", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "user", "picture", "date_posted", "description", "url"]
        read_only_fields = ["date_posted"]


class CommentSerializer(serializers.ModelSerializer):
    pass