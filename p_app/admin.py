from django.contrib import admin

# Register your models here.
from p_app.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created']

