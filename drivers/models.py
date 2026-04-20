from django.db import models
import uuid


class Driver(models.Model):
    STATUS_CHOICES = [
        ('invited', 'Invited'),
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('active', 'Active'),
    ]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    ni_number = models.CharField(max_length=30, blank=True)
    utr_number = models.CharField(max_length=30, blank=True)

    invite_token = models.UUIDField(default=uuid.uuid4, editable=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='invited')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"