from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class OrderItem(models.Model):
    choices = (
        ('Outfit', 'Outfit'),
        ('Furniture', 'Furniture'),
        ('Books', 'Books'),
        ('Gadgets', 'Gadgets')
    )
    item_type = models.CharField(max_length=300, choices=choices)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_type

class IOrder(models.Model):
    customer = models.ForeignKey(Customers, related_name='customers', related_query_name="customer",on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    order_day = models.DateTimeField(auto_now_add=True)
    domestic = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.customer.zip_code == "001":
            return True
        super().save(*args, **kwargs)

