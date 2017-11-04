from django.contrib import admin

from .models import BalanceRecord, Category

admin.site.register([BalanceRecord, Category])
