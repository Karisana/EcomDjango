from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True,verbose_name='Ссылка')

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, verbose_name='Категория')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Фото')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка')
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='Опубликовано')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано в:')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено в:')
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
