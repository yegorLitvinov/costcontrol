from rest_framework import serializers

from .models import BalanceRecord, Category


class BalanceRecordSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField()

    class Meta:
        model = BalanceRecord
        fields = ("id", "amount", "category", "comment", "created_at", "updated_at")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "color", "icon", "kind")


class CategoryStatisticsSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ("id", "name", "color", "total", "kind")


class YearStatisticsSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    category__kind = serializers.CharField()
    total = serializers.IntegerField()

    class Meta:
        fields = ("month", "proceeds", "spendings")


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField(min_value=1990, max_value=2200, required=True)


class MonthOfYearSerializer(YearSerializer):
    month = serializers.IntegerField(min_value=1, max_value=12, required=True)
