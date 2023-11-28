from django.contrib import admin

from .models import Products, Offer


class AdminProducts(admin.ModelAdmin):
	list_display = ('name', 'price', 'stock')

admin.site.register(Products, AdminProducts)
admin.site.register(Offer)
