from rest_framework.pagination import PageNumberPagination

__all__ = ['DefaultPagination']


class DefaultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'count'
    max_page_size = 50
