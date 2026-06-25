from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupons(models.Model):
    code= models.CharField(max_length=16, verbose_name='Промокод')
    discount = models.IntegerField(validators=[MaxValueValidator(99),MinValueValidator(0)])
    valid_from = models.DateTimeField(verbose_name='Начало действия')
    valid_to = models.DateTimeField(verbose_name='Конец действия')
    active = models.BooleanField(default=True)
    apply_now = models.IntegerField(verbose_name='Сколько применено', default=0)
    apply_max = models.IntegerField(verbose_name='Максимально применений')

    def __str__(self):
        return self.code


