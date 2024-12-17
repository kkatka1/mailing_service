from django.utils import timezone

from django.db import models

from users.models import User
from django.contrib.auth import get_user_model

NULLABLE = {"blank": True, "null": True}

User = get_user_model()


class Client(models.Model):
    """Модель Клиент"""

    fullname = models.CharField(max_length=150, verbose_name="ФИО")
    email = models.EmailField(unique=False, verbose_name="Электронная почта")
    comment = models.TextField(max_length=100, verbose_name="Комментарий", null=True)
    user = models.ForeignKey(
        User,
        help_text="Укажите владельца",
        verbose_name="Владелец",
        on_delete=models.CASCADE,
        null=True,
    )

    # mailing_list = models.ManyToManyField(Mailing, verbose_name='Рассылки', related_name='clients_for_mailing')

    def __str__(self):
        return f"{self.fullname} ({self.email})"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ["email", "fullname"]


class Message(models.Model):
    """Модель Сообщение"""

    topic = models.CharField(verbose_name="Тема письма", max_length=30)
    body = models.TextField(verbose_name="Тело письма", max_length=100)
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = [
            "topic",
        ]

    def __str__(self):
        return self.topic


class Mailing(models.Model):
    """Модель Рассылки"""

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    PERIOD_CHOICES = [
        ('day', 'Раз в день'),
        ('week', 'Раз в неделю'),
        ('month', 'Раз в месяц'),
    ]


    date_of_first_dispatch = models.DateTimeField(
        verbose_name="Дата первой отправки рассылки",
        **NULLABLE
    )

    periodicity = models.CharField(
        max_length=10,
        choices=PERIOD_CHOICES,
        verbose_name='Переодичность',
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='created',
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания рассылки", auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name="Дата изменения рассылки", auto_now=True
    )
    message_id = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name="Сообщение",
        help_text="Выберите сообщение",
        related_name="Mailing",
    )
    client_list = models.ManyToManyField(
        Client,
        verbose_name="Клиенты",
        help_text="Выберите клиентов для рассылки",
        related_name="client",
    )

    user = models.ForeignKey(
        User,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Введите владельца",
        on_delete=models.SET_NULL,
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано", help_text="Отметьте для активации"
    )

    def __str__(self):
        return f"{self.message_id}"

    def get_clients(self):
        return ", ".join([client.email for client in self.client_list.all()])

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("created_at",)
        permissions = [
            ("can_view_all_mailing", "Can view all mailing"),
            ("can_disable_mailing", "Can disable mailing"),
        ]


class Attempt(models.Model):
        '''Модель попытки рассылки'''
        STATUS_CHOICES = [
            ('success', 'Успешно'),
            ('failure', 'Неуспешно'),
        ]

        mailing = models.ForeignKey(
            Mailing,
            on_delete=models.CASCADE,
            verbose_name='Рассылка',
            related_name='attempts'
        )
        attempt_date = models.DateTimeField(
            default=timezone.now,
            verbose_name='Дата и время попытки'
        )
        status = models.CharField(
            max_length=10,
            choices=STATUS_CHOICES,
            verbose_name='Статус попытки'
        )
        server_response = models.TextField(
            verbose_name='Ответ почтового сервера',
            blank=True,
            null=True
        )

        def __str__(self):
            return f'Рассылка {self.mailing.id} - {self.get_status_display()} - {self.attempt_date}'

        class Meta:
            verbose_name = 'Попытка рассылки'
            verbose_name_plural = 'Попытки рассылок'