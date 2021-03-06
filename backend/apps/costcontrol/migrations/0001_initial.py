# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 17:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Proceed",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
                ("comment", models.CharField(blank=True, max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["created_at"], "abstract": False},
        ),
        migrations.CreateModel(
            name="ProceedCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("color", models.CharField(max_length=64)),
                ("icon", models.ImageField(upload_to="icons")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="proceed_categories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["id"], "abstract": False},
        ),
        migrations.CreateModel(
            name="Spending",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
                ("comment", models.CharField(blank=True, max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["created_at"], "abstract": False},
        ),
        migrations.CreateModel(
            name="SpendingCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("color", models.CharField(max_length=64)),
                ("icon", models.ImageField(upload_to="icons")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spending_categories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["id"], "abstract": False},
        ),
        migrations.AddField(
            model_name="spending",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="spendings",
                to="costcontrol.SpendingCategory",
            ),
        ),
        migrations.AddField(
            model_name="spending",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="spendings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="proceed",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proceeds",
                to="costcontrol.ProceedCategory",
            ),
        ),
        migrations.AddField(
            model_name="proceed",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proceeds",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
