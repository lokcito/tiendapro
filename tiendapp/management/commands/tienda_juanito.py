from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tiendapp.models import Customer, Order, OrderDetail
from tiendapp.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("tienda tests")
       