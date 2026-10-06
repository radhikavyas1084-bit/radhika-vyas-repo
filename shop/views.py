import random
from datetime import date
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.template import * 
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart

def display(request):
    obj = Product.objects.all()
    return render(request, "display.html", {"x": obj})


def add(request):
    if request.method=="POST":
        n=request.POST.get('n')
        p=request.POST.get('p')
        image=request.FILES.get('image')
        obj=Product(name=n,price=p,image=image)
        obj.save()
        obj=Product.objects.all()
        return render(request,'display.html',context={'x':obj})
    return render(request,'add.html')

def home(request):
    return render(request,"home.html")


def log(request):
    obj=Product.objects.all()
    return render(request,"login.html",context={'x':obj})

def addcart(request, id):

    if request.method == "POST":

        product = get_object_or_404(Product, id=id)

        qty = Decimal(request.POST.get("quantity"))

        item = Cart.objects.filter(product=product).first()

        if item:
            item.quantity += qty
            item.save()
        else:
            Cart.objects.create(
                product=product,
                quantity=qty
            )

    return redirect("display")


def cart(request):

    obj = Cart.objects.all()

    grandtotal = 0

    for i in obj:
        grandtotal += i.total()

    return render(request, "cart.html", {
        "cart": obj,
        "grandtotal": grandtotal
    })

def deletecart(request, id):

    obj = Cart.objects.get(id=id)

    obj.delete()

    return redirect("cart")


def updatecart(request, id):

    obj = Cart.objects.get(id=id)

    if request.method == "POST":

        qty = request.POST.get("quantity")

        obj.quantity = qty

        obj.save()

    return redirect("cart")


from .models import Bill, Cart

def billing(request):

    cart = Cart.objects.all()

    grandtotal = 0

    for i in cart:
        grandtotal += i.total()

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        bill = Bill.objects.create(
            customer_name=name,
            phone=phone,
            address=address,
            grand_total=grandtotal
        )

        return redirect(request,"receipt.html", id=bill.id)

    return render(request, "billing.html", {
        "cart": cart,
        "grandtotal": grandtotal
    })


from django.shortcuts import render, get_object_or_404
from .models import Bill, BillItem

def receipt(request, id):
    bill = get_object_or_404(Bill, id=id)

    items = BillItem.objects.filter(bill=bill)

    return render(request, "receipt.html", {
        "bill": bill,
        "cart": items
    })




