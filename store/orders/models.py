from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

ORDER_STATUS_CHOICES = (
     ('active', 'активный'),
     ('completed', 'завершенный'),
     ('canceled', 'отмененный')
)

class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    phone_number = models.CharField(verbose_name='Телефон',max_length=15)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(verbose_name='Адрес', max_length=128)
    paid = models.BooleanField(default=False, verbose_name='Оплачен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(max_length=20, default='active', choices=ORDER_STATUS_CHOICES, verbose_name='Статус')

    class Meta:
         ordering = ['-created_at']
    
    def __str__(self):
        return f'Заказ № {self.id}'
    
    def get_total_cost(self):
        return sum(item.total_price() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
         return f'{self.id}'

    def total_price(self):
         return self.price * self.quantity