from django.db import models


class Blog(models.Model):
    """Модель блога"""
    heading = models.CharField(max_length=50, verbose_name='Заголовок')
    content_of_article = models.TextField(verbose_name='Содержимое статьи')
    picture = models.ImageField(upload_to='blog/', verbose_name='Изображение')
    number_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    date_of_publication = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
