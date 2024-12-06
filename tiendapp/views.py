from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        "products": [None, None, None, None, None]
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return  render(request, "tiendapp/cart.html", context)

def v_product_detail(request):
    context = {}
    return render(request, 
                  "tiendapp/product_detail.html",
                  context)
    # Completar 
    # crear un diccionario contexto vacio:  context = {}
    # El return render , enlazando el html,  
    # tiendap/product_detail.html
    # Adicionar a la funcion render, contexto