from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from products.models.comment import Comment
from products.serializers.comment_crud import CommentSerializer
from products.serializers.comment_crud import CommentSerializer


class CreateCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
    
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        return Response(
            {"detail": "Comment deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
