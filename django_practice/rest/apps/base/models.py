from django.db import models

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название товара',
    )
    desc = models.TextField(
        verbose_name = 'Описание товара'
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name='URL',
    )
    image = models.ImageField(
        upload_to='tovar/',
        verbose_name = 'Фото товара'
    )
    price = models.IntegerField(
        verbose_name = 'Цена: '
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'