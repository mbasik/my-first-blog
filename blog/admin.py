from django.contrib import admin
from .models import Post, Comment, Place

admin.site.register(Post)
admin.site.register(Place)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)

