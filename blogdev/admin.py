from django.contrib import admin
from .models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)