import datetime

from django.contrib import admin
from django.db.models import Q
from .models import *

admin.site.register(Customers)
admin.site.register(OrderItem)


class CustomersOrderTimeframeFilter(admin.SimpleListFilter):
    title = "Order created timeframe"
    parameter_name = "timeframe"

    def lookups(self, request, model_admin):
        return [
            ("yearly up to today", "This Year Customers")
        ]

    def queryset(self, request, queryset):
        today = datetime.date.today()
        year = today.year
        if self.value() == "yearly up to today":
            return queryset.filter(Q(order_day__date__lte=today) &
                                              Q(order_day__year=year))
        #we would add .count() if we would want to get the count of our queryset
        # however it's already shown in our admin panel

@admin.register(IOrder)
class IOrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_item', "order_day", 'domestic')
    date_hierarchy = 'order_day'
    list_filter = ('domestic', CustomersOrderTimeframeFilter)




