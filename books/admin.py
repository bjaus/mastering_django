from django.contrib import admin
from .models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state_province', 'country')
    ordering = ('name', 'state_province', 'country')
    search_fields = ('name', 'city', 'state_province', 'country')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')
    

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    ordering = ('-publication_date', 'title')
    search_fields = ('title', 'publisher', 'publication_date')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)