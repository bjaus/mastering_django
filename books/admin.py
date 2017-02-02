from django.contrib import admin
from .models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state_province', 'country')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publisher', 'publication_date')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)