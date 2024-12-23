# Generated by Django 5.1.3 on 2024-12-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="заголовок")),
                ("body", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата создания записи"
                    ),
                ),
                (
                    "views_count",
                    models.IntegerField(default=0, verbose_name="Просмотров"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="slug"
                    ),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
    ]
