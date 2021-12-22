from django.shortcuts import render, get_object_or_404, redirect
#from .cart import Cart
from .models import *


def home(request):
    return render(request, 'store/home.html')

def cart(request):
    return render(request, 'store/cart.html')

def contacts(request):
        return render(request, 'store/contacts.html')

def about(request):
    return render(request, 'store/about.html')

def menu(request):
    foods=Food.objects.all()
    context={'foods' : foods}
    return render(request, 'store/menu.html', context)
'''
def cart_add(request,food_id):
    cart=Cart(request)
    product = get_object_or_404(Food,id=food_id)
    return redirct('store/cart.html')

def cart_remove(request,food_id):
    cart=Cart(request)
    product = get_object_or_404(Food,id=food_id)
    cart.remove(product)
    return redirct('store/cart.html')

def cart(request):
    cart=Cart(request)
    return render(request,'store/cart.html',{'cart':cart})

'''
def add_to_cart(request, pk) :
    food = get_object_or_404(Food, pk = pk )
    name = food.name
    #order_item = OrderFood.objects.create(food=food)

    order_qs = Order.objects.filter(username=request.user)

    if order_qs.exists() :
        order = order_qs[0]
        '''
        if order.items.filter(name__pk = name.pk).exists() :
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("store/cart.html", pk = pk)
        else:'''
        order.items.add(food)
        #messages.info(request, "Item added to your cart")
        return render(request, 'store/cart.html')
    else:
        order = Order.objects.create(username=request.user)
        order.items.add(food)
        #messages.info(request, "Item added to your cart")
        return render(request, 'store/cart.html')


def remove_from_cart(request, pk) :
    item = get_object_or_404(Item, pk = pk )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered= False
    )
    if order_qs.exists() :
        order = order_qs[0]
        if order.items.filter(item__pk = item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "Item remove from your cart")
            return redirect("store/cart.html", pk = pk)
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("store/cart.html", pk = pk)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("store/cart.html", pk = pk)
