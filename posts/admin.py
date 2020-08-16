from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'view_count',
        'created_at',
        'updated_at',
        'image',
        'user',
    )
    search_fields = (
        'title',
        'user',
    )
# Register your models here.
