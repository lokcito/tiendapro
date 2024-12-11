from django.shortcuts import render
from tiendapp.models import Product, ProductCategory

# Create your views here.
def v_index(request):
    products_db = Product.objects.all()
    
    context = {
        "products": products_db
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return  render(request, "tiendapp/cart.html", context)

def v_product_detail(request, code):
    product_obj = Product.objects.get(sku = code)

    # Obtener las categorias del producto
    categories_obj = [c.category_id for c in ProductCategory
                      .objects.filter(product = product_obj)]
    
    # categories_obj almacena datos como:  [4 , 5, 6, 88]
    # [4 , 5, 6, 88] estos numeros son los ids de las categorias
    
    # De las categorias obtenidas
    # Filtrar los productos relacionados
    pc_obj = ProductCategory.objects.filter(category__id__in = categories_obj)
    extras = []
    for pc in pc_obj:
        extras.append(pc.product)

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