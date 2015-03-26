from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    user = models.OneToOneField(User)
    
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
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Address(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    userProfile = models.ForeignKey(UserProfile)
    
    BILLING = 'bill'
    SHIPPING = 'ship'
    BOTH = 'both'
    ADDRESS_TYPE_CHOICES = (
                            (BILLING, 'Billing'),
                            (SHIPPING, 'Shipping'),
                            (BOTH, 'Both')
                            )
    
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    zip = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    address_type = models.CharField(max_length=4,
                                      choices=ADDRESS_TYPE_CHOICES,
                                      default=BOTH)
    
    def __str__(self):
        return "%s %s, %s %s" % (self.zip, self.city, self.street, self.street_number)
    