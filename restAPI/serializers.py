from rest_framework import serializers
from users.models import Profile
from feed.models import Post, Comment
from django.shortcuts import get_object_or_404


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )

    # user = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "image", "bio", "url"]

    # def get_user(self, obj):
    #     return obj.user.username


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["user", "comment", "comment_date"]
        read_only_fields = ["comment_date"]

    def get_user(self, obj):
        return obj.user.username


class PostUserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail", read_only=True
    )

    user = serializers.CharField(source="user.username")

    class Meta:
        model = Profile
        fields = ["id", "user", "url"]


class PostSerializer(serializers.ModelSerializer):
    # user = PostUserSerializer(read_only=True, source="user.username")
    # user = PostUserSerializer

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
        read_only_fields = ["user", "date_posted"]


# make a postcreate serializer to make a post request


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = PostUserSerializer(many=True, read_only=True, source="post_user")
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
