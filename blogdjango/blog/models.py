from django.db import models
from django.urls import reverse

class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    title = models.CharField(max_length=222, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='images/news/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_detail', kwargs={'pk': self.pk})



class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категоии'
        ordering = ['title']

    title = models.CharField(max_length=222, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})










