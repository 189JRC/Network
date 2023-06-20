from django.contrib import admin
from .models import Profile, Post, User, Contact

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(User)
