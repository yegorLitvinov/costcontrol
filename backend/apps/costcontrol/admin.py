from django.contrib import admin

from .models import Proceed, ProceedCategory, Spending, SpendingCategory

admin.site.register([ProceedCategory, SpendingCategory, Proceed, Spending])
