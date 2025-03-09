"""
URL configuration for backed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights import views as flights_views
from user import views as user_views
from orders import views as order_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('back/update/', flights_views.update_flights, name='update_flight'),
    path('back/flights/', flights_views.get_flights, name='get_flights'),
    path('back/flights/<int:flight_id>/', flights_views.get_flight, name='get_flight'),
    path('api/register/', user_views.register),
    path('api/login/', user_views.login),
    path('api/user/<int:user_id>/', user_views.get_user_token),
    path('api/user/<int:user_id>/tickets/', order_views.get_user_tickets),
    path('api/order/create/', order_views.create_order),
    path('api/user/update/', user_views.update_user_info),
    path("api/user/forget/", user_views.forget_password),
]