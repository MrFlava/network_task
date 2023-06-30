from rest_framework.serializers import ModelSerializer, DateField, IntegerField

from posts.models import Post, Like


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "text")

    def create(self, validated_data):
        data = validated_data.copy()
        data["user_created"] = self.context["request"].user

        return super().create(data)


class PostUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "text")
        read_only_fields = ("user_created", )


class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = ("post", )

    def create(self, validated_data):
        data = validated_data.copy()
        data["liked_by"] = self.context["request"].user

        return super().create(data)


class LikeByDaySerializer(ModelSerializer):
    date_liked = DateField()
    likes = IntegerField()

    class Meta:
        model = Like
        fields = ('date_liked', 'likes')

