from django.contrib import admin
from .models import Aircraft, Flight
from django.http import JsonResponse
from django.urls import path
from datetime import datetime
from zoneinfo import ZoneInfo
from django.db import IntegrityError
from .flightSpider import getFlights

admin.site.register(Aircraft)
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_no', 'departure_time', 'departure_city', 'arrival_city', 'price', 'airline')
    list_filter = ('departure_city', 'arrival_city', 'airline', 'departure_time')
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-flights/', self.admin_site.admin_view(self.import_flights), name='flights_flight_import-flights'),
        ]
        return custom_urls + urls

    def import_flights(self, request):
        if request.method == 'POST':
            departure_city = request.POST.get('departure_city')
            arrival_city = request.POST.get('arrival_city')

            if not departure_city or not arrival_city:
                return JsonResponse({'status': 'error', 'message': '请输入出发地和目的地'})
            print(departure_city, arrival_city)
            data = getFlights(departure_city, arrival_city)
            print(len(data))
            # print(data)
            try:
                default_aircraft = Aircraft.objects.first()
                success_count = 0

                for item in data:
                    flight_no = item['flightNo']

                    price = item['price']
                    if price is None or price == '':
                        price = 1000
                        # continue 
                    # print(item)
                    # 处理出发时间
                    depart_datetime_str = f"{item['departDate']} {item['departTime'].strip()}"
                    depart_naive = datetime.strptime(depart_datetime_str, "%Y-%m-%d %H:%M")
                    depart_aware = depart_naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
                    # 处理到达时间
                    arrive_datetime_str = f"{item['departDate']} {item['arriveTime'].strip()}"
                    arrive_naive = datetime.strptime(arrive_datetime_str, "%Y-%m-%d %H:%M")
                    arrive_aware = arrive_naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
                    # 检查 flight_no 是否已存在
                    if Flight.objects.filter(flight_no=flight_no, departure_time=depart_aware).exists():
                        continue  # 跳过已存在的相同航班
                    # print(item)
                    try:
                        Flight.objects.create(
                            flight_no=flight_no,
                            departure_city=departure_city,
                            arrival_city=arrival_city,
                            departPortName=item['departPortName'],
                            arrivePortName=item['arrivePortName'],
                            departure_time=depart_aware,
                            arrival_time=arrive_aware,
                            price=price,
                            aircraft=default_aircraft,
                            airline=item['airlineCompanyName'],
                        )
                        success_count += 1
                    except IntegrityError as e:
                        print(f"IntegrityError: {e}")
                        continue  # 跳过引发异常的数据

                return JsonResponse({'status': 'success', 'message': f"{success_count}条航班数据已成功导入！"})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f"导入失败: {str(e)}"})

        return JsonResponse({'status': 'error', 'message': '无效请求'})

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['batch_import'] = True
        return super().changelist_view(request, extra_context=extra_context)