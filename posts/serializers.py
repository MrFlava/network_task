from rest_framework.serializers import ModelSerializer

from posts.models import Post


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
