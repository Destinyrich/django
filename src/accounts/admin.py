from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser




from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GuestEmail, EmailActivation

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# class UserAdmin(BaseUserAdmin):
#     # Import the forms here to delay their import
#     from .forms import UserAdminCreationForm, UserAdminChangeForm

#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'admin')
#     list_filter = ('admin', 'staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('full_name', 'email', 'password')}),  # Define necessary fields
#         ('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email', 'full_name',)
#     ordering = ('email',)
#     filter_horizontal = ()



# # class UserAdmin(BaseUserAdmin):
# #     # The forms to add and change user instances
# #     form = UserAdminChangeForm
# #     add_form = UserAdminCreationForm

# #     # The fields to be used in displaying the User model.
# #     # These override the definitions on the base UserAdmin
# #     # that reference specific fields on auth.User.
# #     list_display = ('email', 'admin')
# #     list_filter = ('admin', 'staff', 'is_active')
# #     fieldsets = (
# #         (None, {'fields': ('full_name', 'email', 'password')}),
# #        # ('Full name', {'fields': ()}),
# #         ('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
# #     )
# #     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
# #     # overrides get_fieldsets to use this attribute when creating a user.
# #     add_fieldsets = (
# #         (None, {
# #             'classes': ('wide',),
# #             'fields': ('email', 'password1', 'password2')}
# #         ),
# #     )
# #     search_fields = ('email', 'full_name',)
# #     ordering = ('email',)
# #     filter_horizontal = ()


# # admin.site.register(User, UserAdmin)

# # # Remove Group Model from admin. We're not using it.
# # admin.site.unregister(Group)



# # class EmailActivationAdmin(admin.ModelAdmin):
# #     search_fields = ['email']
# #     class Meta:
# #         model = EmailActivation


# # admin.site.register(EmailActivation, EmailActivationAdmin)


# # class GuestEmailAdmin(admin.ModelAdmin):
# #     search_fields = ['email']
# #     class Meta:
# #         model = GuestEmail


# # admin.site.register(GuestEmail, GuestEmailAdmin)