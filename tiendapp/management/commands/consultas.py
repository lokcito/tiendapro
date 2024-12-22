from django.core.management.base import BaseCommand
from tiendapp.models import Product, ProductCategory, Order,\
    OrderDetail, Customer
from django.contrib.auth.models import User

class Command(BaseCommand):
    def query_1(self):
        #Contar todas las ordenes
        norders = Order.objects.all().count()
        #         TRAE A TODAS LAS OR|CONTAR 

        print("El numero de ordenes es: " + str(norders))

    def query_2(self):
        # Contar todos los clientes
        # Customer.objects.all().count() => Returna numero
        ncustomers = Customer.objects.all().count()
        print("El numero de clientes es: " + str(ncustomers))

    def query_3(self):
        # Contar a los usuarios que no son clientes
        # User.objects.all() => QuerySet => Lista
        contador = 0
        for us in User.objects.all():
            # Cuando no exista un registro Customer para el usuario US
            # Customer.objects.filter(user = us).exists() => Retorna Booleano
            if not Customer.objects.filter(user = us).exists():
                contador = contador + 1
        print("Los usuarios que no son clientes son: " + str(contador))

    def query_4(self):
        # Filtrar a los clientes por nombre
        #   M____campo_uno
        # Filtra por nombre exacto
        c = Customer.objects.filter(
            user__first_name = "Hans") #=> QuerySet => Lista 

        print("Filtrado de clientes (exacto): ", c)

        #__contains => like %Hans%
        c = Customer.objects.filter(
            user__first_name__contains = "ans") #=> QuerySet => Lista 

        print("Filtrado de clientes (like): ", c)

        #__contains => ilike %Hans%
        c = Customer.objects.filter(
            user__first_name__icontains = "hans") #=> QuerySet => Lista 

        print("Filtrado de clientes (ilike): ", c)

    def query_5(self):
        #Filtrar a las ordenes por nombre de cliente
        orders = Order.objects.filter(customer__user__first_name = "Hans")
        print("Ordenes de Hans: ", orders)
    
    def query_6(self):
        #Mostrar a las ordenes ordenadas por ID desc
        print("Ordenes: ")
        orders = Order.objects.all().order_by("-id")
        for ord in orders:
            print(ord.id, "|", ord.customer)
    
    def query_7(self):
        print("Customers: ")
        customers = Customer.objects.all().order_by("-user__last_name")
        for cust in customers:
            print(cust.id, cust.user.last_name)
        
    def query_8(self):
        print("Ordenes pendientes:")
        orders = Order.objects.filter(status = "PENDIENTE")
        for ord in orders:
            print(ord.id, "|", ord.customer.user.first_name)

    def query_9(self):
        print("Creando 5 clientes: ")

        def create_user(_username):
            us = User.objects.filter(username = _username).first()
            if us is not None:
                return us
            else:
                us = User()
                us.username = _username
                us.first_name = "FN_" + _username
                us.save()
                return us
        
        def create_customer(_user):
            cust = Customer.objects.filter(user = _user).first()
            if cust is not None:
                return cust
            else:
                cust = Customer()
                cust.user = _user
                cust.save()

        for contador in range(0, 5):
            tmp_user = create_user("US" + str(contador))
            create_customer(tmp_user)
        
        print("# Customers: ", Customer.objects.all().count())

    def handle(self, *args, **kwargs):
        queries = [
            "1.- Contar todas las ordenes",
            "2.- Contar todos los clientes",
            "3.- Contar a los usuarios que no son clientes",
            "4.- Filtrar a los clientes por nombre",
            "5.- Filtrar a las ordenes por nombre de cliente",
            "6.- Mostrar a las ordenes ordenadas por ID desc",
            "7.- Mostrar a los clientes ordenados por Apellido desc",
            "8.- Filtrar a las ordenes en pendiente",
            "9.- Crear 5 clientes.",
            "10.- Crear 5 usuarios de Django",
            "11.- Crear 5 productos."
        ]
        for query in queries:
            print(query)
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.query_1()
        elif opcion == "2":
            self.query_2()
        elif opcion == "3":
            self.query_3()
        elif opcion == "4":
            self.query_4()
        elif opcion == "5":
            self.query_5()
        elif opcion == "6":
            self.query_6()
        elif opcion == "7":
            self.query_7()
        elif opcion == "8":
            self.query_8()
        elif opcion == "9":
            self.query_9()
