from rest_framework import serializers

from .models import Proceed, ProceedCategory, Spending, SpendingCategory


class BalanceRecordSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField()

    class Meta:
        fields = ('id', 'amount', 'comment', 'user',
                  'created_at', 'updated_at', 'category')


class SpendingSerializer(BalanceRecordSerializer):
    class Meta:
        model = Spending
        fields = BalanceRecordSerializer.Meta.fields


class ProceedSerializer(BalanceRecordSerializer):
    class Meta:
        model = Proceed
        fields = BalanceRecordSerializer.Meta.fields


class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'color', 'icon')


class ProceedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProceedCategory
        fields = ('id', 'name', 'color', 'icon')


class SpeindingCategoryStatisticSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'color', 'total')


class ProceedCategoryStatisticSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = ProceedCategory
        fields = ('id', 'name', 'color', 'total')
