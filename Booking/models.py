from django.db import models


class TableBook(models.Model):
    date = models.DateField()
    time = models.TimeField()
    person = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    occasion = models.CharField(max_length=50,blank=True)
    special_request = models.TextField(blank=True)

    class Meta:
        verbose_name = "Table Book"
        verbose_name_plural = "Table Books"

    def __str__(self):
        return self.name

