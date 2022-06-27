from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created

from .models import ConfirmEmailToken, User

from celery import shared_task


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    

    msg = EmailMultiAlternatives(

        f"Password Reset Token for {reset_password_token.user}",

        reset_password_token.key,

        settings.EMAIL_HOST_USER,

        [reset_password_token.user.email]
    )
    msg.send()


@shared_task
def new_user_registered(user_id, **kwargs):
    r
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(

        f"Password Reset Token for {token.user.email}",

        token.key,

        settings.EMAIL_HOST_USER,

        [token.user.email]
    )
    msg.send()


@shared_task
def new_order(user_id, **kwargs):

    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(

        f"Обновление статуса заказа",

        'Заказ сформирован',

        settings.EMAIL_HOST_USER,

        [user.email]
    )
    msg.send()