from rest_framework                       import generics, status
from commentApp.models.comment                  import Comment
from commentApp.serializers.commentSerializer   import CommentSerializer
from rest_framework.response import Response

# Create
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *arg, **kwargs):

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Comentario creado", status=status.HTTP_201_CREATED)

# Read
class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs['post'])
        return queryset

# Delete
class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):           
        queryset = Comment.objects.filter(user=self.kwargs['user'])
        return queryset

    def delete(self, request, *arg, **kwargs):        
        return super().destroy(request, *arg, **kwargs)

# Update 
class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(user=self.kwargs['user'])
        return queryset

    def put(self, request, *arg, **kwargs):
        return super().update(request, *arg, **kwargs)


