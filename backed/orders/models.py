from django.db import models
from django.utils import timezone
from user.models import UserInfo
from flights.models import Flight
from flights.models import Seat

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True, editable=False, verbose_name='订单号')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 使用 'user' 更符合惯例
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='航班信息')  # 使用 'flight' 更符合惯例
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='orders', verbose_name='座位号')
    name = models.CharField(max_length=100, verbose_name='姓名')
    passportNo = models.CharField(max_length=20, verbose_name='身份证/护照')
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, verbose_name='购买日期')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='等待出行')

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = timezone.now().strftime('%Y%m%d%H%M%S')
        super(Order, self).save(*args, **kwargs)
    
    def cancel(self):
        # 更新座位状态
        self.seat.status = 'available'
        self.seat.save()

        # 更新订单状态
        self.status = '已取消'
        self.save()

    def __str__(self):
        # 简化了对象的字符串表示，方便调试和日志记录。
        return f"订单： {self.order_id}， 用户： {self.user} 下单时间： {self.date}"

    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = '订单信息'

class TicketNotification(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='notifications')
    sent_at = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
    # 当你打印TicketNotification对象时，它将调用__str__(self),返回一个字符串，表示该通知的订单ID和发送时间
        return f'订单 {self.order.order_id} 取票通知'
    class Meta:
        verbose_name = '取票通知表'
        verbose_name_plural = '取票通知信息'

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invoices')
    issued_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='未支付')

    def __str__(self):
        return f'订单 {self.order.order_id} 账单'
    class Meta:
        verbose_name = '账单表'
        verbose_name_plural = '账单信息'