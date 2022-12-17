from django.contrib import admin
from blog.models import Post


admin.site.register(Post)
#test123
#
# @admin.site.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#
#
