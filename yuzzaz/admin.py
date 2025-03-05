from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Coordinator

# Admin for CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    list_filter = ['is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'password')}), 
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'is_staff'),
        }),
    )

# Register CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)

# Admin for Coordinator model
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_user_email', ]
    search_fields = ['user__email', 'user__first_name', 'user__last_name']

    def save_model(self, request, obj, form, change):
        if not change and Coordinator.objects.exists():
            raise ValueError("Only one Coordinator can be added.")
        super().save_model(request, obj, form, change)

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = "User Email"

    # def get_user_phone(self, obj):
    #     return obj.user.phone_number
    # get_user_phone.short_description = "User Phone"
    
admin.site.register(Coordinator, CoordinatorAdmin)
