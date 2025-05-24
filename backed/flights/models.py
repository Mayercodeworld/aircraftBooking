from django.db import models
# Create your models here.
class Aircraft(models.Model):
    model = models.CharField(max_length=50, unique=True)
    total_seats = models.IntegerField()

    def __str__(self):
        return f'机型: {self.model}, 总座位数: {self.total_seats}'

    class Meta:
        verbose_name = '飞机类型表'
        verbose_name_plural = '飞机型号'

# 航班表
class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=16, verbose_name='航班号')
    departure_city = models.CharField(max_length=8, verbose_name='出发城市')
    arrival_city = models.CharField(max_length=8, verbose_name='到达城市')
    arrivePortName = models.CharField(max_length=20)
    departPortName = models.CharField(max_length=20)
    departure_time = models.DateTimeField(verbose_name='出发时间')
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='flights')  # 外键到Aircraft
    airline = models.CharField(max_length=100, default='UnKnown', verbose_name='航空公司') 


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def remaining_seats(self):
        # 获取飞机的总座位数
        total_seats = self.aircraft.total_seats if self.aircraft else 0

        # 查询当前航班中 status='booked' 的座位数量
        booked_count = self.seats.filter(status='booked').count()

        # 剩余座位 = 总座位 - 已预订
        return max(total_seats - booked_count, 0)

    def __str__(self):
        return f'航班 {self.flight_no}:  {self.departure_city} - {self.arrival_city}'

    class Meta:
        verbose_name = '航班表'
        verbose_name_plural = '航班信息'


# 座位表
class Seat(models.Model):
    SEAT_STATUS_CHOICES = [
        ('available', '可选'),
        ('booked', '已预订'),
    ]

    # SEAT_TYPE_CHOICES = [
    #     ('economy', '经济舱'),
    #     ('business', '商务舱'),
    #     ('first_class', '头等舱'),
    # ]

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='seats')  # 关联航班
    seat_number = models.CharField(max_length=10)  # 座位号，例如 A1, B2
    # seat_type = models.CharField(max_length=20, choices=SEAT_TYPE_CHOICES)  # 座位类型
    status = models.CharField(max_length=20, choices=SEAT_STATUS_CHOICES, default='available')  # 座位状态

    def __str__(self):
        return f"{self.seat_number} ({self.status})"
    class Meta:
        verbose_name = '座位表'
        verbose_name_plural = '座位信息信息'
