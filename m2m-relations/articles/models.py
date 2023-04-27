from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    tags = models.ManyToManyField(Tag, through='Scope', verbose_name='Теги', related_name='articles')
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег', related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        unique_together = ['is_main']

    def __str__(self):
        return f'{self.article}: {self.tag}'

