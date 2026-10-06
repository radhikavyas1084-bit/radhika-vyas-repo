from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Product List
    path("display/", views.display, name="display"),
    path("log/", views.log, name="log"),

    # Add Product
    path("add/", views.add, name="add"),

    # Add To Cart
    path("addcart/<int:id>/", views.addcart, name="addcart"),

    # Cart Page
    path("cart/", views.cart, name="cart"),

    # Update Quantity
    path("updatecart/<int:id>/", views.updatecart, name="updatecart"),

    # Delete Cart Item
    path("deletecart/<int:id>/", views.deletecart, name="deletecart"),

    # Billing Page
   #path("billing/", views.billing, name="billing"),

    # Place Order
    #path("placeorder/", views.placeorder, name="placeorder"),

    # Receipt
   #path("receipt/<int:id>/", views.receipt, name="receipt"),
   path("billing/", views.billing, name="billing"),
path("receipt/<int:id>/", views.receipt, name="receipt"),
]

