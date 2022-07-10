from django.utils.timezone import now
from rest_framework import filters
from rest_framework.settings import api_settings

__all__ = ['NearBirthdayFilter']


class NearBirthdayFilter(filters.BaseFilterBackend):
    ordering_param = api_settings.ORDERING_PARAM
    ordering_field = 'birthday'

    def filter_queryset(self, request, queryset, view):
        if request.query_params.get(self.ordering_param) == self.ordering_field:
            today = now().date().replace(year=2020)

            return queryset.filter(birthday__gte=today).order_by(self.ordering_field) | \
                queryset.filter(birthday__lt=today).order_by(self.ordering_field)

        return queryset
