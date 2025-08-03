from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from products.models import Upload
from products.serializers import UploadSerializer


class UploadImageView(CreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    parser_classes = (MultiPartParser, FormParser)
