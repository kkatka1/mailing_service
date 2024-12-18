from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    body = models.TextField(verbose_name="содержимое")
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(
        blank=True, null=True, verbose_name="Дата создания записи"
    )
    views_count = models.IntegerField(default=0, verbose_name="Просмотров")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.CharField(max_length=150, verbose_name="slug", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
