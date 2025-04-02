from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import User, Service

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("date_joined",)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'is_partner')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'is_partner', 'is_superuser',
                       'is_staff', 'is_active')}
         ),
    )
    filter_horizontal = ()
    inlines = [ServiceInline]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Service)
