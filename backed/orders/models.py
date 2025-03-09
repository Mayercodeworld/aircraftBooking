from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    order_id = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.order_id} by User {self.user_id} on {self.date}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'