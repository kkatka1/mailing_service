from config.settings import EMAIL_HOST_USER
from django.utils import timezone
from django.core.mail import send_mail
from mailing.models import Mailing, Attempt


def send_newsletters():
    now = timezone.now()
    mailings = Mailing.objects.filter(
        scheduled_at__lte=now,
        status='started'
    )

    for mailing in mailings:
        # Логика отправки рассылки
        try:
            # Перебираем клиентов и отправляем письма
            for client in mailing.clients.all():
                send_mail(
                    mailing.message_id.topic,
                    mailing.message_id.body,
                    EMAIL_HOST_USER,
                    [client.email],
                )

            # Запись попытки рассылки как успешной
            Attempt.objects.create(
                newsletter=mailing,
                status='success'
            )

            # Обновляем дату последней отправки
            mailing.last_run = now
            mailing.save()

            # Обработка периодичности рассылки
            if mailing.periodicity == 'day':
                mailing.scheduled_at += timezone.timedelta(days=1)
            elif mailing.periodicity == 'week':
                mailing.scheduled_at += timezone.timedelta(weeks=1)
            elif mailing.periodicity == 'month':
                mailing.scheduled_at += timezone.timedelta(weeks=4)

            # Обновление статуса рассылки
            mailing.status = 'started'
            mailing.save()

        except Exception as e:
            # Если произошла ошибка, записываем это как неуспешную попытку
            Attempt.objects.create(
                newsletter=mailing,
                status='failure',
                server_response=str(e)
            )
