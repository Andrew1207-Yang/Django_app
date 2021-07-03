from django.db import models
from django.db.models.fields import CharField, EmailField, TextField
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    name = CharField(max_length = 100)
    message = TextField(blank=False, null=False)
    email = EmailField(blank=False, null=False)

    def get_absolute_url(self):
        return '#contact'