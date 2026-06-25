from django.shortcuts import redirect
from coupons.forms import CouponApplyForm
from coupons.models import Coupons
from django.utils import timezone
from django.views.decorators.http import require_POST

@require_POST
def coupon_apply(request):
    time_now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupons.objects.get(code__iexact=code,
                                    valid_from__lte=time_now,
                                    valid_to__gte=time_now)
            print(coupon.code)
            coupon.apply_now += 1
            coupon.save()
            request.session['coupon_id'] = coupon.id
        except Coupons.DoesNotExist:
            print('купон не найден')
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
