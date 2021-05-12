from django.db import models

# Create your models here.
#1 Категории
#2 Продукт
#3 Карта продукта
#4 Корзина
#5 Заказ
#6 Покупатель
#7 Спецификации



class Category(models.Model):

    name = models.CharField(max_lenght=255,verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
