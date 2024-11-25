from django.contrib import admin
from .models import Category, Drink, Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'table', 'guest_count', 'date', 'time', 'email')
    list_filter = ('date', 'time', 'table')
    search_fields = ('name', 'email')
    ordering = ('-date', '-time')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;"/>'
        return "No image"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"
