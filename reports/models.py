from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('Phone', 'Phone'),
    ('Wallet', 'Wallet'),
    ('Bag', 'Bag'),
    ('Laptop', 'Laptop'),
    ('Keys', 'Keys'),
    ('Other', 'Other'),
]

class LostItems(models.Model):
    name = models.CharField(max_length=50)
    date_lost = models.DateField()
    location = models.TextField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class FoundItem(models.Model):
    name = models.CharField(max_length=200)
    date_found = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name