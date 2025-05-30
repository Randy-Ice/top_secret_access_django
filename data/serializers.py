from rest_framework.serializers import ModelSerializer

from data.models import BlogsLevelOne


class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogsLevelOne
        fields = [
            'id', 'title', 'body', 'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']