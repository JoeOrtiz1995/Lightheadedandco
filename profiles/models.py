from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from products.models import Product

# Create your models here.


class UserProfile(models.Model):
    """
    Stores a User's Profile information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates a profile or updates an existing one
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class Wishlist(models.Model):
    """
    Stores a user's wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist_items = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"Wishlist for: {self.user.username}"


@receiver(post_save, sender=User)
def create_or_update_wishlist(sender, instance, created, **kwargs):
    """
    Creates a wishlist or updates an existing one
    """
    if created:
        Wishlist.objects.create(user=instance)
