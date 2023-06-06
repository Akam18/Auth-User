from django.db import models
from .utils import valid_price


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255,  verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural ="Категории"


class Product(models.Model):
    image = models.ImageField(upload_to="Productivity")
    title = models.CharField(max_length=225, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(default=10.0, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return f"{self.title} - {self.category} - {self.created_at}"


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"