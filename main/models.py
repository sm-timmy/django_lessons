from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

