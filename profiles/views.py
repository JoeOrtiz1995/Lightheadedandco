from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Product

# Create your views here.
def profile(request):
  """
  Dispalys a User's profile
  """
  profile = get_object_or_404(UserProfile, user=request.user)

  if request == 'POST':
    form = UserProfileForm(request.POST, instance=profile)
    if form.is_valid():
      form.save()
      messages.success(request, ('Your profile has been updated'))

  form = UserProfileForm(instance=profile)
  orders = profile.orders.all()

  template = 'profiles/profile.html'
  context = {
    'form': form,
    'orders': orders,
    'on_profile_page': True,
  }

  return render(request, template, context)


def order_history(request, order_number):
  order = get_object_or_404(Order, order_number=order_number)

  messages.info(request, (f'This is a confirmation for order number: {order_number}.'))

  template = 'checkout/checkout_success.html'
  context = {
    'order': order,
    'from_profile': True,
  }

  return render(request, template, context)


def view_wishlist(request):
  """
  A view to return a page with the User's bag contents.
  """
  wishlist, created = Wishlist.objects.get_or_create(user=request.user)
  template = 'profiles/wishlist.html'
  context = {
    'wishlist': wishlist,
  }

  return render(request, template, context)


def add_to_wishlist(request, item_id):
  """
  Adds products to a user's wishlist
  """
  product = get_object_or_404(Product, pk=item_id)
  wishlist, created = Wishlist.objects.get_or_create(user=request.user)
  wishlist.wishlist_items.add(product)
  wishlist.save()
  return redirect("view_wishlist")
  
def remove_from_wishlist(request, item_id):
  """
  Returns the user's wishlist without the removed item
  """
  product = get_object_or_404(Product, pk=item_id)
  wishlist = Wishlist.objects.get(user=request.user)
  wishlist.wishlist_items.remove(product)
  wishlist.save()
  return redirect("view_wishlist")
