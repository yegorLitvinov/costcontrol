# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 09:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.forms.models import model_to_dict


def fill_new_with_old(apps, schema_editor):
    """
    Only one db table for balance records and categories
    """
    SpendingCategory = apps.get_model('costcontrol', 'SpendingCategory')
    ProceedCategory = apps.get_model('costcontrol', 'ProceedCategory')

    BalanceRecord = apps.get_model('costcontrol', 'BalanceRecord')
    Category = apps.get_model('costcontrol', 'Category')

    for proceed_category in ProceedCategory.objects.all():
        proceed_category_values = model_to_dict(proceed_category)
        proceed_category_values.pop('id')
        proceed_category_values['user_id'] = proceed_category_values.pop('user')
        proceed_category_values['kind'] = 'proceed'
        category = Category.objects.create(**proceed_category_values)
        for proceed_values in proceed_category.proceeds.all().values():
            proceed_values.pop('user_id')
            proceed_values.pop('id')
            proceed_values['category_id'] = category.id
            BalanceRecord.objects.create(**proceed_values)

    for spending_category in SpendingCategory.objects.all():
        spending_category_values = model_to_dict(spending_category)
        spending_category_values.pop('id')
        spending_category_values['user_id'] = spending_category_values.pop('user')
        spending_category_values['kind'] = 'spending'
        category = Category.objects.create(**spending_category_values)
        for spending_values in spending_category.spendings.all().values():
            spending_values.pop('user_id')
            spending_values.pop('id')
            spending_values['category_id'] = category.id
            BalanceRecord.objects.create(**spending_values)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('costcontrol', '0001_initial'),
    ]

    operations = [
        # Create new models
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('color', models.CharField(max_length=64)),
                ('icon', models.ImageField(upload_to='icons')),
                ('kind', models.CharField(choices=[('proceed', 'Proceed'), ('spending', 'Spending')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='BalanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('comment', models.CharField(blank=True, max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_records', to='costcontrol.Category')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),

        # Fill new models with data from old models
        migrations.RunPython(fill_new_with_old),

        # Delete old models
        migrations.RemoveField(
            model_name='proceed',
            name='category',
        ),
        migrations.RemoveField(
            model_name='proceed',
            name='user',
        ),
        migrations.RemoveField(
            model_name='proceedcategory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='category',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='user',
        ),
        migrations.RemoveField(
            model_name='spendingcategory',
            name='user',
        ),
        migrations.DeleteModel(
            name='Proceed',
        ),
        migrations.DeleteModel(
            name='ProceedCategory',
        ),
        migrations.DeleteModel(
            name='Spending',
        ),
        migrations.DeleteModel(
            name='SpendingCategory',
        ),
    ]
