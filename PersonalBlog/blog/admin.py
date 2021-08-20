from django.contrib import admin
from .models import Post, Contact


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
