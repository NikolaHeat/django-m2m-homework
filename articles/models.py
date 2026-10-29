from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    published_at = models.DateTimeField(
        verbose_name='Дата публикации'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название раздела'
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name='Статья'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Раздел'
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Основной раздел'
    )

    class Meta:
        verbose_name = 'Раздел статьи'
        verbose_name_plural = 'Разделы статей'
        constraints = [
            models.UniqueConstraint(
                fields=['article', 'tag'],
                name='unique_article_tag'
            )
        ]

    def __str__(self):
        return f'{self.article.title} — {self.tag.name}'