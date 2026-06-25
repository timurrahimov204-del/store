class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon = self.session.get('coupon_id')

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    

    def __len__(self):
       return sum(item['quantity'] for item in self.cart.values()) 
    

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in =products_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item 
    
    def get_total_price_with_sale(self):
        coupon = Coupons.objects.get(id = self.session.get('coupon_id'))
        return self.get_total_price() * (100 - coupon.discount) / 100
    
    def remove_coupon(self):
        del self.session['coupon_id']
        self.save()