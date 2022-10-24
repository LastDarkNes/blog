from django.contrib import admin
from .models import Post, Category, Comment


class NewAdmin(admin.ModelAdmin):
    list_display = ['category', ...]


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
