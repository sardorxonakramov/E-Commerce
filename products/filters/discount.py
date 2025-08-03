from django_filters import rest_framework as django_filters

from products.models.discount import Discount


class DiscountFilter(django_filters.FilterSet):
    percentage_min = django_filters.NumberFilter(field_name="percentage", lookup_expr="gte")
    percentage_max = django_filters.NumberFilter(field_name="percentage", lookup_expr="lte")
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    expires_after = django_filters.DateTimeFilter(field_name="expired_at", lookup_expr="gte")
    expires_before = django_filters.DateTimeFilter(field_name="expired_at", lookup_expr="lte")

    class Meta:
        model = Discount
        fields = ["product", "percentage", "price", "expired_at"]
