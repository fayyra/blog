from django.contrib import admin
from .models import Blog, Comment, Profile


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'text')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')


admin.site.register(Comment)
admin.site.register(Profile, ProfileAdmin)
