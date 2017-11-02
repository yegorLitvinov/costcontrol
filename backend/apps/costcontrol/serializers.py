from rest_framework import serializers

from .models import Proceed, ProceedCategory, Spending, SpendingCategory


class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'color', 'icon')


class SpendingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField(required=True)

    class Meta:
        model = Spending
        fields = ('id', 'amount', 'comment', 'user',
                  'created_at', 'updated_at', 'category')


class ProceedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProceedCategory
        fields = ('id', 'name', 'color', 'icon')


class ProceedSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField(required=True)

    class Meta:
        model = Proceed
        fields = ('id', 'amount', 'comment', 'user',
                  'created_at', 'updated_at', 'category')


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
