from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product, Contact, Order, OrderUpdate
import json
from math import ceil
# Create your views here.
def index(request):
    allProducts=[]
    ProductCategory = Product.objects.values("category", "id")
    Categories = {item["category"] for item in ProductCategory}
    for Cat in Categories:
        Products = Product.objects.filter(category=Cat)
        n = len(Products)
        nSlides = n//4 + ceil((n/4) - (n//4))   
        allProducts.append([Products, range(1, nSlides), nSlides])
    params = {'allProducts':allProducts}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name=request.POST.get('name' ,'')
        email=request.POST.get('email' ,'')
        phone=request.POST.get('phone' ,'')
        desc=request.POST.get('desc' ,'')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})

def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemjson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')

def searchmatch(query, item):
    #return only if query matches the item
    query = str(query)
    price = str(item.price)
    if query in item.product_name.lower() or query in item.product_desc.lower() or query in item.category.lower() or query in price:
        return True
    else:
        return False

def search(request):
    #take a query from search and process it here and return the relevent results.
    query = request.GET.get('search')
    allProducts=[]
    ProductCategory = Product.objects.values("category", "id")
    # print(ProductCategory)
    Categories = {item["category"] for item in ProductCategory}
    # print(Categories)
    for Cat in Categories:
        # print(Cat)
        Prodtemp = Product.objects.filter(category=Cat)
        # print(Prodtemp)
        prod = [item for item in Prodtemp if searchmatch(query, item)]
        # print(prod)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        if len(prod) !=0 :   
            allProducts.append([prod, range(1, nSlides), nSlides])
    params = {'allProducts':allProducts, 'message':""}
    if len(allProducts) == 0 or len(query) < 2:
        params = {'message':"Please enter a relevent product info."}
    return render(request, 'shop/search.html', params)

def productView(request, myid):
    # Fetch the product using id
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request, 'shop/productview.html',{'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_Json = request.POST.get('itemsJson', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address1', "") + " " + request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        pin_code = request.POST.get('pin_code', "")
        phone = request.POST.get('phone', "")

        order = Order(items_json = items_Json, name = name, email = email, address = address, city = city, state = state, pin_code = pin_code, phone = phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc='The Order has been placed!')
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')