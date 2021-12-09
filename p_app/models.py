from django.db import models

# Create your models here.
from django.views.generic import CreateView


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

