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
            # Здесь вы должны указать, как отправить сообщения
            # Например, если у вас есть список клиентов
            for client in mailing.clients.all():
                send_mail(
                    mailing.message.title,
                    mailing.message.message,
                    EMAIL_HOST_USER,
                    [client.email],
                )

            # Запись попытки рассылки
            Attempt.objects.create(
                newsletter=mailing,
                status='success'
            )

            # Обновляем дату последней отправки
            mailing.last_run = now
            mailing.save()

            # Проверяем периодичность
            if mailing.periodicity == 'day':
                mailing.scheduled_at += timezone.timedelta(days=1)
            elif mailing.periodicity == 'week':
                mailing.scheduled_at += timezone.timedelta(weeks=1)
            elif mailing.periodicity == 'month':
                mailing.scheduled_at += timezone.timedelta(weeks=4)

            # Если запланирована новая отправка, сохраняем статус как 'started'
            mailing.status = 'started'  # можно оставить или изменить статус по вашему желанию
            mailing.save()

        except Exception as e:
            # Если произошла ошибка, записываем это в попытку рассылки
            Attempt.objects.create(
                newsletter=mailing,
                status='failure',
                server_response=str(e)
            )