from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    description_main = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=False)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title

