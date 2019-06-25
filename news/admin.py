from django.contrib import admin

# Register your models here.

from .models import News, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name','cat_slug')
    prepopulated_fields = {'cat_slug': ('cat_name',)}
    fieldsets = [
        ('Name', {'fields': ['cat_name']}),
        (None, {'fields': ['cat_slug']}),
    ]

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on','category')
    list_filter = ['created_on']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    fieldsets = [
        ('Main Info', {'fields': ['title','slug']}),
        (None,{'fields': [('author','status','category')]}),
        ('Content', {'fields': ['content']}),
        ('Main Image', {'fields': ['cover']}),
    ]

admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)