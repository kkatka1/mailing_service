from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """ Модель Клиент """

    fullname = models.CharField(max_length=150, verbose_name="ФИО")
    email =  models.EmailField(unique=False, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, unique=True)
    comment = models.TextField(max_length=100,verbose_name="Комментарий", null=True)
    country = models.CharField(max_length=50, verbose_name='Страна', null=True)
    timezone = models.CharField(max_length=50, verbose_name='Время', null=True)
    #owner = models.ForeignKey(User, help_text='Укажите владельца', verbose_name='Владелец',on_delete = models.CASCADE)
    # mailing_list = models.ManyToManyField(Mailing, verbose_name='Рассылки', related_name='clients_for_mailing')

    def __str__(self):
        return f'{self.fullname} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ["email", "fullname"]


class Message(models.Model):
    """Модель Сообщение"""

    topic = models.CharField(verbose_name="Тема письма", max_length=30)
    body = models.TextField(verbose_name="Тело письма", max_length=100)
    #owner = models.ForeignKey(User,verbose_name="Пользователь",on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = [
            "topic",
        ]

    def __str__(self):
        return self.topic


class Mailing(models.Model):
    """ Модель Рассылки """
    date_of_first_dispatch = models.DateTimeField(verbose_name="Дата первой отправки рассылки", **NULLABLE)
    periodicity = models.CharField(max_length=1, choices=[("1", "Один раз в день"), ("2", "Один раз в неделю"), ("3", "Один раз в месяц")], verbose_name="Периодичность отправки", help_text="Выберите периодичность отправки", **NULLABLE)
    status = models.CharField(max_length=20, choices=[("A", "Создана"), ("B", "Запущена"), ("C", "Завершена")], verbose_name="Статус рассылки")
    created_at = models.DateTimeField(verbose_name="Дата создания рассылки", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата изменения рассылки", auto_now=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", help_text="Выберите сообщение", related_name='Mailing')
    client_list = models.ManyToManyField(Client, verbose_name='Клиенты', help_text='Выберите клиентов для рассылки', related_name='client')
    #client_list = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='mailing_for_mailing')
    #owner = models.ForeignKey(User, **NULLABLE, verbose_name='Владелец', help_text='Введите владельца',on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано", help_text="Отметьте для активации")

    def __str__(self):
        return f"{self.message_id.title}"

    def get_clients(self):
        return ", ".join([client.email for client in self.client_list.all()])

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("created_at",)
        permissions = [
            ("Can_is_published", "Can is published"),
        ]

class Attempt(models.Model):
    """ Модель Логов """
    date_last_attempt = models.DateTimeField(verbose_name="Дата последней попытки", auto_now=True)
    status = models.BooleanField(verbose_name="Статус рассылки")
    server_response = models.CharField(max_length=50, verbose_name="Ответ сервера")
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка", help_text="Выберите рассылку", related_name='Attempt')
    #owner = models.ForeignKey(User, **NULLABLE, verbose_name='Владелец', help_text='Введите владельца',on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.date_last_attempt}"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ("status",)