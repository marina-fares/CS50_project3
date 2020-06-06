from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu,Order
from django.http import JsonResponse

import datetime



# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    context ={
        'order' : Order.objects.filter(customer = request.user),
    }
    return render(request, 'profile.html', context)


def menu_view(request):
    if request.method == 'POST':
        var = request.POST.getlist("exampleFormControlSelect1")
        item_size = []
        for item in var:
            item_size.append(item[-16:-11])   
        order = Order(customer= request.user, item_size= item_size, datetime= datetime.datetime.now())
        order.save()
        for item in var:
            item_id = int(item[-20:-17])
            order.item_id.add(item_id)
        return render(request, 'profile.html')
    context = {
          "menu": Menu.objects.all()
      }
    return render(request, "menu.html",context)
