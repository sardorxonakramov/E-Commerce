from django.urls import path
from products.views.comment_crud import CreateCommentAPIView, UpdateDeleteCommentAPIView


urlpatterns = [
    path("", CreateCommentAPIView.as_view(), name="comment-create"),  # POST
    path(
        "<int:pk>/", UpdateDeleteCommentAPIView.as_view(), name="comment-update-delete"
    ),  # PUT, DELETE
]
