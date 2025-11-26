from django.shortcuts import render
from .serializer import LostItemSerializer, FoundItemSerializer
from reports.models import LostItems, FoundItem
from rest_framework import viewsets, filters
from rest_framework.generics import RetrieveAPIView
from reports.utils import match_lost_item
from rest_framework.decorators import action
from rest_framework.response import Response


class LostItemsViewset(viewsets.ModelViewSet):
    queryset = LostItems.objects.all()
    serializer_class = LostItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location', 'description']
    ordering_fields = ['name', 'date_lost', 'location']

    @action(detail=True, methods=["get"])
    def matches(self, request, pk=None):
        """
    GET /api/lost-items/<id>/matches/
    Returns a list of found items with match scores.
        """
        lost_item = self.get_object()  # Get lost item by ID
        found_items = FoundItem.objects.all()  # Fetch all found items from DB
        matches = match_lost_item(lost_item, found_items)  # Pass both arguments
        return Response(matches)

class FoundItemViewset(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location', 'description']
    ordering_fields = ['name', 'date_found', 'location']

