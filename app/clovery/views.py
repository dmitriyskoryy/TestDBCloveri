from datetime import datetime

from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    """Домашняя страница. Общая для всех - и авторизованных и не авторизованных"""
    def get(self, request):

        product = Product.objects.exclude(name__in=Order.objects.values('name_product__name').filter(user_order__date_creation__gte='2023-02-01'))


        # product = Product.objects.exclude(name__in=Order.objects.values('name_product__name').all())
        product2 = Product.objects.all()


        # Entry.objects.filter(pub_date__date__gte=datetime.date(2023, 2, 1))

        context = {
            'info': product,
            'info2': product2,
        }
        return render(request, "index.html", context)
