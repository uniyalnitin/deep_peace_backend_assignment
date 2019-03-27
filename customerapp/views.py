from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import User
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import BaseFilterBackend

class CustomSearchFilter(filters.SearchFilter):
    search_param = 'name'

class CustomOrderingFilter(filters.OrderingFilter):
    ordering_param = 'sort'

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size =  50

class UserView(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    related_model = User
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (CustomSearchFilter, CustomOrderingFilter,)
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['age']

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.GET.get('name',None)
        sort_by = self.request.GET.get('sort', None)

        if username is not None:
            queryset = queryset.filter(first_name__icontains=username) | queryset.filter(last_name__icontains=username)
        if sort_by is not None:
            queryset = queryset.order_by(sort_by)
        return queryset
