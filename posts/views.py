from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-update_at')
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
