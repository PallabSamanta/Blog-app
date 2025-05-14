from django.contrib import admin
from .models import Post, Comment
from .models import SavedPost

admin.site.register(Post)
admin.site.register(Comment)

@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'saved_at')
    list_filter = ('user', 'saved_at')
    search_fields = ('user__username', 'post__title')