from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from catalog.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')



def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = CartAddProductForm(initial={'quantity':item['quantity'], 'override':True})
    coupon_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_form': coupon_form})
