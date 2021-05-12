from django.db import models

# Create your models here.
#1 Категории
#2 Продукт
#3 Корзина продукта
#4 Корзина
#5 Заказ
#6 Покупатель
#7 Спецификации



class Category(models.Model):

    name = models.CharField(max_lenght=255,verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_lenght=255,verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class CartProduct(models.Model):

    user = modeles.ForeidnKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = modeles.ForeidnKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    product = modeles.ForeidnKey('Product', verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegrField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return f"Продукт: {self.product.title} (для корзины)"

