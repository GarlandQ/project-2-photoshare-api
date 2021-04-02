from rest_framework import serializers
from users.models import Profile
from feed.models import Post, Comment
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "image", "bio"]

    # id = serializers.IntegerField(read_only=True)
    # user = serializers.CharField()
    # image = serializers.ImageField()
    # bio = serializers.CharField(max_length=255, allow_blank=True)

    # def create(self, validated_data):
    #     return Profile.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get("user", instance.user)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.bio = validated_data.get("bio", instance.bio)
    #     instance.save()
    #     return instance
