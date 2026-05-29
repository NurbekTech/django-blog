from django.contrib import admin
from apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "published", "status"]
    list_filter = ["status", "created", "published", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["author"]
    date_hierarchy = "published"
    ordering = ["status", "published"]
    list_select_related = ["author"]
