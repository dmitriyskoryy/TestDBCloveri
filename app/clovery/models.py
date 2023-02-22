from django.db import models


class CategoryMenu(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(CategoryMenu, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.name}'


class UsersOrder(models.Model):
    user = models.CharField(max_length=128)
    order_number = models.SmallIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')

    def __str__(self):
        return f'{self.user} {self.order_number}'


class Order(models.Model):
    user_order = models.ForeignKey(UsersOrder, on_delete=models.CASCADE)
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_order} {self.name_product}'