import os
from datetime import timedelta, datetime

from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import make_aware


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='drinks', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='drinks_images/', blank=True, null=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Drink)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_image = Drink.objects.get(pk=instance.pk).image
    except Drink.DoesNotExist:
        return

    new_image = instance.image
    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


@receiver(post_delete, sender=Drink)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"


class Booking(models.Model):
    table = models.ForeignKey(Table, related_name='bookings', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    guest_count = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"

    @staticmethod
    def is_table_available(table, date, time, duration=2):
        start_time = make_aware(datetime.combine(date, time))
        end_time = start_time + timedelta(hours=duration)

        overlapping_bookings = Booking.objects.filter(
            table=table,
            date=date,
            time__gte=(start_time - timedelta(hours=duration)).time(),
            time__lt=end_time.time()
        )

        return not overlapping_bookings.exists()
