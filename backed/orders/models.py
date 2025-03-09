from django.db import models
from django.utils import timezone
from user.models import UserInfo
from flights.models import Flight

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True, editable=False)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 使用 'user' 更符合惯例
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)  # 使用 'flight' 更符合惯例
    name = models.CharField(max_length=100)
    passportNo = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='等待出行')

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = timezone.now().strftime('%Y%m%d%H%M%S')
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"订单： {self.order_id}， 用户： {self.user} 下单时间： {self.date}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'