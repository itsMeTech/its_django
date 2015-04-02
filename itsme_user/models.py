from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class ItsmeUserManager(BaseUserManager):
    def _create_user(self, email, password, is_client, is_staff, is_superuser):
        if not email:
            raise ValueError('Users must have an email address')
                
        now = timezone.now()
        email = self.normalize_email(email)
        username = self.generate_username(email)
        itsme_email = self.generate_itsme_email(username)
        is_active = True
        
        user = self.model(
            email=email,
            username=username,
            itsme_email=itsme_email,
            is_client=is_client,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        is_client = False
        is_staff = False
        is_staff = False
        return self._create_user(email, password, is_client, is_staff, False)

    def create_superuser(self, email, password):
        return self._create_user(email, password, False, True, True)
    
    def generate_username(self, email, i=0):
        
        if i==0:
            username = str(email.split('@')[0]) 
        else:
            username = str(email.split('@')[0]) + str(i)

        try:
            get_user_model().objects.get(username=username)
            i+=1
            return self.generate_username(email=email, i=i)
        except get_user_model().DoesNotExist:
            return username;
    
    def generate_itsme_email(self, username):
        itsme_email=username + '@itsme.app'
        return self.normalize_email(itsme_email);

class ItsmeUser(AbstractBaseUser, PermissionsMixin):
    # The following attributes are inherited from the superclasses:
    #    * password
    #    * last_login
    #    * is_superuser

    # Validator for phone numbers regarding internationally standardized format E.164
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    # Redefine the basic fields that would normally be defined in User
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField('email address', unique=True, max_length=255, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))    
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    
    # Our own fields
    itsme_email = models.EmailField('itsme email address', unique=True, max_length=255)
    is_client = models.BooleanField(default=False, help_text=_(
            'Designates whether the user is part of a client.'))
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    
    objects = ItsmeUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.itsme_mail

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.emai