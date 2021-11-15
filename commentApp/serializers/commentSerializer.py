from commentApp.models.comment import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','user', 'post', 'datepublished','image']

