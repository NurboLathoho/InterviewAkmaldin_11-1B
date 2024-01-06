from django.db import models

class Settings(models.Model):
    image = models.ImageField(
        upload_to='order/',
        verbose_name = 'Изображение',
    )
    title = models.CharField(
        max_length=255,
        verbose_name = 'Название товара'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
    