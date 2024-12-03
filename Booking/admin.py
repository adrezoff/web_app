from django.contrib import admin
from .models import TableBook, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')


@admin.register(TableBook)
class TableBookAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'person', 'table', 'name')
