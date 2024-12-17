from django.db import models

import token

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        null=True,
        blank=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=40,
        verbose_name="Страна",
        null=True,
        blank=True,
        help_text="Введите название страны",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватвр",
        null=True,
        blank=True,
        help_text="Загрузите свой аватар",
    )

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ('can_change_user_status', "Can change user status"),
            ("can_block_user", "Can block user"),
        ]

    def __str__(self):
        return self.email
