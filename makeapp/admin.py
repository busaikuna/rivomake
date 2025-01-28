from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Produto
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfis'
    list_display = ('user', 'foto')
    search_fields = ('user__username',)

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,) 
    list_display = ('username', 'email', 'is_staff', 'is_active')  
    search_fields = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Produto)
