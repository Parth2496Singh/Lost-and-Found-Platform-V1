from rest_framework import serializers
from reports.models import LostItems, FoundItem

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItems
        fields = '__all__'

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'