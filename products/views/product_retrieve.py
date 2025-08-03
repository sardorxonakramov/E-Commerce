# from rest_framework import generics, status
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

# from products.models import Product
# from products.serializers import ProductRetrieveSerializer
# # from product.services.product import ProductService
# from stream.models import Stream


# class ProductRetrieveView(generics.RetrieveAPIView):
#     """
#     View for retrieving and creating products.
#     """

#     queryset = Product.objects.all()
#     service_class = ProductService
#     permission_classes = [AllowAny]
#     serializer_class = ProductRetrieveSerializer

#     def get(self, request, *args, **kwargs):
#         key = request.query_params.get("key")
#         if key:
#             ip_address = request.META.get("REMOTE_ADDR")
#             Stream.objects.create(key_id=key, ip_address=ip_address)

#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
