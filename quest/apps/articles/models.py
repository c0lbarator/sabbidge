import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def lol(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    au_name = models.CharField('Имя автора', max_length=45)
    comment = models.CharField('Текст комментария', max_length=200)

    def __str__(self):
        return self.au_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'