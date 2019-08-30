from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    PERMISSIONS = (
        ('0', 'Collaborator'),
        ('1', 'Admin'),
    )
    permissions = models.CharField(
        max_length=1,
        choices=PERMISSIONS,
        blank=True,
        default='0',
    )
