from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu,Order
from django.http import JsonResponse

import datetime



# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu_view(request):
    context = {
          "menu": Menu.objects.all()
      }
    
    return render(request, "menu.html",context)

def run_python_script(request):
    os.system('python3 main_chatbot.py')
    return HttpResponse("OK")

def save_order(request):
    if request.user.is_authenticated:
        var = request.POST.getlist("exampleFormControlSelect1")
        item_size = []
        for item in var:
            item_size.append(item[-6:-1])    
        order = Order(customer= request.user, item_size= item_size, datetime= datetime.datetime.now())
        order.save()
        for item in var:
            item_id = int(item[-11:-7])
            order.item_id.add(item_id)
    return HttpResponse(var)


def show_order(request):
    if request.user.is_authenticated:
        var = request.POST.getlist("exampleFormControlSelect1")
        total_price = 0
        item_size = []
        item_and_size = []
        items_and_sizes = []
        for item in var:
            item_size.append({int(item[-11:-7]) : item[-6:-1]})    
        
        for item in item_size:
            for key, value in item.items():
                item_details = Menu.objects.filter(pk=key)
                item_and_size.append(item_details)
                item_and_size.append(value)
                items_and_sizes.append(item_and_size)
                item_and_size = []

                if value == 'Small':
                    total_price += item_details[0].price_small
                elif value == 'Large':
                    total_price += item_details[0].price_large
        request.session['items'] = item_size
        context={
            "items" : items_and_sizes,
            "total_price" : total_price      
        }
    return render(request, 'order.html', context)


def send_order(request):
    items_and_sizes = request.session['items']
    list_of_ids = []
    list_of_sizes = []
    for item in items_and_sizes:
        for key, value in item.items():
            list_of_ids.append(int(key))
            list_of_sizes.append(value)
    order = Order(customer= request.user, item_size= list_of_sizes, datetime= datetime.datetime.now())
    order.save()
    for item in list_of_ids:
        order.item_id.add(item)
    return HttpResponse(items_and_sizes)



