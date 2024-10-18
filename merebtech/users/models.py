from django.conrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('agent', 'Agent'),
        ('player', 'Football Player'),
    ]

    role = models.CharField(max_length=10, choices=USER_ROLES, default='player')


    def __str__(self):
        return self.username
    
