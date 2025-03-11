from django.db import models
import random
# Create your models here.
class Aircraft(models.Model):
    model = models.CharField(max_length=50, unique=True)
    total_seats = models.IntegerField()

    def __str__(self):
        return f'机型: {self.model}, 总座位数: {self.total_seats}'

    class Meta:
        verbose_name = 'Aircraft'
        verbose_name_plural = 'Aircrafts'

# 航班表
class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=10, unique=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='flights')  # 外键到Aircraft
    airline = models.CharField(max_length=100, default='UnKnown') 

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # 检查是否是新创建的实例
        super().save(*args, **kwargs)
        if is_new:
            # 如果是新建航班，则创建座位
            seats = Seat.generate_seat_numbers(self)
            Seat.objects.bulk_create(seats)
    def get_booked_seats(self):
        return self.seats.filter(status='booked').count()

    def get_available_seats(self):
        return self.aircraft.total_seats - self.get_booked_seats()
    
    def calculate_fullness_rate(self):
        booked_seats = self.get_booked_seats()
        return (booked_seats / self.aircraft.total_seats) * 100

    def __str__(self):
        return f'航班 {self.flight_no}:  {self.departure_city} 到 {self.arrival_city}'

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'


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

    @classmethod
    def generate_seat_numbers(cls, flight):
        # 限制座位字母为 A, B, C, D, E, F
        seat_letters = 'ABCDEF'
        total_seats = flight.aircraft.total_seats
        seats = []

        # 计算每个字母对应的座位数
        seats_per_letter = total_seats // len(seat_letters)
        remaining_seats = total_seats % len(seat_letters)

        for i, letter in enumerate(seat_letters):
            # 计算当前字母的座位数
            num_seats_for_letter = seats_per_letter
            if i < remaining_seats:
                num_seats_for_letter += 1

            for number in range(1, num_seats_for_letter + 1):
                seat_number = f'{letter}{number}'
                seats.append(Seat(flight=flight, seat_number=seat_number))

        return seats
    @classmethod
    def get_sequential_seat(cls, flight, seat_letter):
        # 获取指定字母的可用座位，并按行数排序
        available_seats = cls.objects.filter(
            flight=flight,
            seat_number__startswith=seat_letter,
            status='available'
        ).order_by('seat_number')

        if available_seats.exists():
            # 按顺序分配第一个可用座位
            seat_to_book = available_seats.first()
            seat_to_book.status = 'booked'
            seat_to_book.save()
            return seat_to_book
        else:
            # 如果没有可用座位，随机分配一个其他座位
            all_available_seats = cls.objects.filter(flight=flight, status='available')
            if all_available_seats.exists():
                seat_to_book = random.choice(all_available_seats)
                seat_to_book.status = 'booked'
                seat_to_book.save()
                return seat_to_book
            else:
                raise Exception("所有座位都已被占用")

    @classmethod
    def book_seat(cls, flight, seat_letter):
        try:
            return cls.get_sequential_seat(flight, seat_letter)
        except Exception as e:
            raise e
        