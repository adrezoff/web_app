from django.contrib.auth import get_user_model
from django.db import models

from Account.models import CustomUser


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"


class TableBook(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    person = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    special_request = models.TextField(blank=True)

    class Meta:
        verbose_name = "Table Book"
        verbose_name_plural = "Table Books"

    def __str__(self):
        return f"{self.name} - Table {self.table}"

