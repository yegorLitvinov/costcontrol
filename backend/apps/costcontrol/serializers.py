from rest_framework import serializers

from .models import BalanceRecord, Category


class BalanceRecordSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField()

    class Meta:
        model = BalanceRecord
        fields = ('id', 'amount', 'category', 'comment',
                  'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'color', 'icon', 'kind')


class CategoryStatisticSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'color', 'total', 'kind')
