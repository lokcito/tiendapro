from django.shortcuts import redirect, render
from tiendapp.models import Product, ProductCategory, Customer
from tiendapp.models import OrderDetail, Order

# Create your views here.
def v_index(request):
    products_db = Product.objects.all()
    
    context = {
        "products": products_db
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    customer_obj = Customer.objects.get(user = request.user)

    order_current = customer_obj.get_current_order()
    # order_current tipo: Order
    details = OrderDetail.objects.filter(order = order_current)
    #details array de : OrderDetail
    context = {
        "items": details
    }
    return  render(request, "tiendapp/cart.html", context)

def v_product_detail(request, code):
    product_obj = Product.objects.get(sku = code)

    rels = ProductCategory.objects.filter(product = product_obj)

    # rels_ids, guarda los ids categoria del producto
    rels_ids = [rr.category.id for rr in rels]
    sug = ProductCategory.objects.filter(
        category__in = rels_ids).exclude(product = product_obj)
    
    # sug, posee a las sugerencias, pero necesito los ids de los productos
    sug_ids = [ss.product.id for ss in sug]
    
    extras = Product.objects.filter(id__in = sug_ids)

    context = {
        "product": product_obj,
        "extras": extras
    }
    return render(request, 
                  "tiendapp/product_detail.html",
                  context)
    # Completar 
    # crear un diccionario contexto vacio:  context = {}
    # El return render , enlazando el html,  
    # tiendap/product_detail.html
    # Adicionar a la funcion render, contexto

def v_add_to_cart(request, code):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    # Algoritmos nuevos
    # Procesar 
    product_obj = Product.objects.get(sku = code)
    # request.user, guarda variable de sesion
    customer_obj = Customer.objects.get(user = request.user)

    orden_current = customer_obj.get_current_order()

    # Verifica que si existe un producto seleccionado previamente
    detail_obj = OrderDetail.objects.filter(product = product_obj, 
                            order = orden_current).first()

    if detail_obj is not None: # Actualiza price
        detail_obj.price = product_obj.price
        detail_obj.save()
    else: # Crear item en carrito
        detail_obj = OrderDetail()
        detail_obj.product = product_obj
        detail_obj.order = orden_current
        detail_obj.quantity = 1
        detail_obj.price = product_obj.price
        detail_obj.save()
    return redirect("/cart")

def v_remove_from_cart(request, code):
    # eliminar
    product_obj = Product.objects.get(sku = code)

    customer_obj = Customer.objects.get(user = request.user)

    current_order = customer_obj.get_current_order()

    item_cart = OrderDetail.objects.filter(
        order = current_order,
        product = product_obj
    ).first()

    if item_cart is not None:
        item_cart.delete()

    return redirect("/cart")