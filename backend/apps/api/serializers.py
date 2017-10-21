from rest_framework import serializers

from apps.costcontrol.models import Proceed, ProceedCategory, Spending, SpendingCategory


class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'color', 'icon')


class SpendingSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Spending
        fields = ('id', 'amount', 'comment', 'created_at', 'updated_at', 'category')


class ProceedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProceedCategory
        fields = ('id', 'name', 'color', 'icon')


class ProceedSerializer(serializers.ModelSerializer):
    # category__name = serializers.SlugRelatedField(read_only=True, slug_field='name')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Proceed
        fields = ('id', 'amount', 'comment', 'created_at', 'updated_at', 'category')


class SpeindingCategoryStatisticSerializer(serializers.ModelSerializer):
    total_spendings = serializers.IntegerField()

    class Meta:
        model = SpendingCategory
        fields = ('id', 'name', 'color', 'total_spendings')


class ProceedCategoryStatisticSerializer(serializers.ModelSerializer):
    total_proceeds = serializers.IntegerField()

    class Meta:
        model = ProceedCategory
        fields = ('id', 'name', 'color', 'total_proceeds')
