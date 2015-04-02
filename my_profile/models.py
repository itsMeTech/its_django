from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
                      (MALE, 'male'),
                      (FEMALE, 'female'),
                      )
    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    title = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    


class Address(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    BILLING = 'bill'
    SHIPPING = 'ship'
    BOTH = 'both'
    ADDRESS_TYPE_CHOICES = (
                            (BILLING, 'Billing'),
                            (SHIPPING, 'Shipping'),
                            (BOTH, 'Both')
                            )
    
    #user = models.ForeignKey(AuthUser)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    zip = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    address_type = models.CharField(max_length=4,
                                      choices=ADDRESS_TYPE_CHOICES,
                                      default=BOTH)
    