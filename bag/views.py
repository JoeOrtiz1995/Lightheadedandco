from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """
    A view to return a page with the User's bag contents.
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Adds products to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f'{bag[item_id]} x {product.name} in your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} is now in your bag')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Updates the quantity of a specified product in the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         f'{bag[item_id]} x {product.name} in your bag')
    else:
        bag.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Removes a specified product in the bag
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'There has been an error removing this item: {e}')
        return HttpResponse(status=500)
