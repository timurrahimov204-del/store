from django.conf import settings
from orders.models import Order
from django.core.mail import EmailMessage
from celery import shared_task


@shared_task
def order_created_send_email(order_id):
    order = Order.objects.get(id=order_id)
    email = EmailMessage(
        subject=f'Ваш заказ {order_id} от {order.created_at.strftime('%d.%m.%Y %H:%m')}',
        body=f'Заказ {order_id} успешно выполнен!\n\n Спасибо за покупку!',
        from_email=settings.EMAIL_HOST_USER,
        to=[order.email]
    )
    email.send()