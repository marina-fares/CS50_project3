from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Menu,Order
from django.http import JsonResponse
from django.contrib import messages


import datetime
import ast




def home(request):
    return render(request, 'home.html')

def profile(request):

    orders_dict = {}
    sizes=[]
    list_order = []
    list_orders = []
    list_item_foreach_order = []
    list_of_items_and_sizes = []
    list_of_all_orders = []
    
    list_size = Order.objects.filter(customer = request.user).values_list('item_size')
    orders = Order.objects.filter(customer = request.user).all()
    

    for l_size in list_size:
        sizes.append(ast.literal_eval(l_size[0]))

    for order in orders:
        list_orders.append(order)
    
    for order in list_orders:

        for item in order.item_id.all():
            list_item_foreach_order.append(item)
        for item_new in list_item_foreach_order:
            list_order.append(item_new)
            list_order.append(sizes[list_orders.index(order)][list_item_foreach_order.index(item)])
            list_of_items_and_sizes.append(list_order)
            list_order = []
        list_item_foreach_order = []
            
        list_of_all_orders.append(list_of_items_and_sizes)
        list_of_items_and_sizes = []
    
    

    for order in list_orders:
        orders_dict[order.datetime] = list_of_all_orders[list_orders.index(order)] 
    
    context ={
        'orders' : orders_dict,  
    }
    return render(request, 'profile.html', context)


def menu_view(request):
    context = {
          "menu": Menu.objects.all()
      }
    if request.method == 'POST':
        var = request.POST.getlist("exampleFormControlSelect1")
        item_size = []
        for item in var:
            if 'Small' in item:
                item_size.append('Small')
            else:
                item_size.append('Large')
        order = Order(customer= request.user, item_size= item_size, datetime= datetime.datetime.now())
        order.save()
        for item in var:
            item_id = int(item[item.find(':')+len(':'):item.rfind('+')])
            order.item_id.add(item_id)
        if(len(var)==0):
            order.delete()
            messages.error(request, 'you have to select at least one item')
            return render(request, "menu.html",context)
        messages.success(request, 'Your order has been submitted')
        return redirect('orders:profile')
    return render(request, "menu.html",context)
