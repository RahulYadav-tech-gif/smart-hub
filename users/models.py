from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    city = models.CharField(max_length=100, blank=True)
    last_login_view = models.DateTimeField(auto_now=True)
    interests = models.TextField(blank=True, null=True) # Text field for multiple interests
    city = models.CharField(max_length=100, blank=True, null=True) # Char field for city



    def __str__(self):
        return f"{self.user.username} Profile"
