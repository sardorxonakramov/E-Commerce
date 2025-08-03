from django_filters import rest_framework as django_filters

from products.models.product import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price"]
