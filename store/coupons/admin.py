from coupons.models import Coupons
from django.contrib import admin


@admin.register(Coupons)
class CouponsAdmin(admin.ModelAdmin):
    create_coupon = ['code', 'discount', 'valid_from', 'valid_to', 'apply_max']

