from rest_framework import serializers
from users.models import Profile
from feed.models import Post, Comment
from django.shortcuts import get_object_or_404


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )

    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "image", "bio", "url"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["user", "comment", "comment_date"]
        read_only_fields = ["comment_date"]


class PostUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )

    user = serializers.CharField(source="user.username")

    class Meta:
        model = Profile
        fields = ["id", "user", "url"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = PostUserSerializer(source="user.profile", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name="post-detail", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "picture",
            "date_posted",
            "comments",
            "description",
            "url",
        ]
        read_only_fields = ["date_posted"]


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = PostUserSerializer(source="user.profile", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name="post-detail", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "picture",
            "date_posted",
            "comments",
            "description",
            "url",
        ]
        read_only_fields = ["picture", "date_posted"]
