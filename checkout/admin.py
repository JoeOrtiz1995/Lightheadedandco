from django.contrib import admin
from .models import Order, OrderLineItem

# Models registered:


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'grand_total',
                       'original_bag', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'county', 'grand_total',
              'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
