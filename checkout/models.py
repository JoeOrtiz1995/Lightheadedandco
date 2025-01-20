import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

# Create your models here.
class Order(models.Model):
  """
  Stores a user's Order
  """
  order_number = models.CharField(max_length=32, null=False, editable=False)
  full_name = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(max_length=254, null=False, blank=False)
  phone_number = models.CharField(max_length=20, null=False, blank=False)
  country = models.CharField(max_length=40, null=False, blank=False)
  postcode = models.CharField(max_length=20, null=True, blank=True)
  town_or_city = models.CharField(max_length=40, null=False, blank=False)
  street_address1 = models.CharField(max_length=80, null=False, blank=False)
  county = models.CharField(max_length=80, null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

  def _generate_order_number(self):
    """
    Generates a unique order number using UUID
    """
    return uuid.uuid4().hex.upper()

  def update_total(self):
    """
    Updates the order's total whenever new lines are added
    """
    self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
    self.save()

  def save(self, *args, **kwargs):
    """
    Replaces an existing order's number, or assigns it a new one
    """
    if not self.order_number:
      self.order_number = self._generate_order_number()
    super().save(*args, **kwargs)

  def __str__(self):
    return self.order_number


class OrderLineItem(models.Model):
  """
  Stores the information for each item in a user's order, related to model:`checkout.Order`
  """
  order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
  product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
  quantity = models.IntegerField(null=False, blank=False, default=0)
  lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

  def save(self, *args, **kwargs):
    """
    Updates the lineitem's total value, and then the order's total accordingly
    """
    self.lineitem_total = self.product.price * self.quantity
    super().save(*args, **kwargs)

  def __str__(self):
    return f'SKU {self.product.name} on order {self.order.order_number}'