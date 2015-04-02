from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ItsmeUserChangeForm, ItsmeUserCreationForm
from .models import ItsmeUser
from django.utils.translation import ugettext_lazy as _

class ItsmeUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'username', 'itsme_email', 'phone', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_client', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_client', 'is_staff', 'is_superuser')}
        ),
    )
    
    # The forms to add and change user instances
    form = ItsmeUserChangeForm
    add_form = ItsmeUserCreationForm
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_client', 'is_staff')
    list_filter = ('is_client', 'is_staff', 'is_superuser', 'is_active', 'groups')    

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register the new ItsmeUserAdmin
admin.site.register(ItsmeUser, ItsmeUserAdmin)