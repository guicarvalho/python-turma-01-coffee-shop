from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.stock <= 2:
        send_mail(
            'Estoque baixo',
            f'Favor comprar mais {instance.description}, estoque atual é de {instance.stock}.',
            'coffeeshop@noreply.com.br',
            ['9c3e57d9f2@mailox.biz'],
            fail_silently=False,
        )

