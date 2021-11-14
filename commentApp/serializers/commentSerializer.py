from commentApp.models.comment import Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content','user', 'post', 'datepublished','image']

